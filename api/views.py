from datetime import timedelta

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils import timezone
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import (CourseSerializer, CustomUserSerializer,
                             KnowledgeBaseSerializer, ProjectSerializer,
                             QuestionTestSerializer, SpecializationSerializer,
                             UserSkillSerializer)
from career_toolbox.models import (Course, Grade, KnowledgeBase, Project,
                                   Specialization)
from quiz.models import AnswerTest, QuestionTest
from users.models import User, UserSkill

from .utils import is_test_available_for_user


class UserSkillViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет для модели UserSkill.
    """
    serializer_class = UserSkillSerializer

    def get_queryset(self):
        user = self.request.user
        return UserSkill.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        user = self.request.user
        user_grade = user.grades.first().title

        skills_lists = {}

        for level in range(1, 4):
            skills_lists[level] = []

        for user_skill in queryset:
            if user_skill.level in skills_lists:
                skills_lists[user_skill.level].append(
                    UserSkillSerializer(user_skill).data
                )

        skills_to_improve = []
        achieved_skills = []

        if user_grade == settings.JUNIOR_GRADE:
            skills_to_improve.extend(skills_lists[1])
            achieved_skills.extend(skills_lists[2] + skills_lists[3])
        elif user_grade == settings.MIDLE_GRADE:
            skills_to_improve.extend(skills_lists[2])
            achieved_skills.extend(skills_lists[1] + skills_lists[3])
        elif user_grade == settings.SENIOR_GRADE:
            achieved_skills.extend(
                skills_lists[1] + skills_lists[2] + skills_lists[3]
            )

        result_data = {
            "skillsToImprove": skills_to_improve,
            "achievedSkills": achieved_skills,
        }

        return Response(result_data)


class CustomUserViewSet(UserViewSet):
    """
    Вьюсет для модели User.
    """
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели Project.
    """
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        user_specializations = user.specializations.all()
        return Project.objects.filter(
            specializations__in=user_specializations
        ).distinct()


class KnowledgeBaseViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели KnowledgeBase.
    """
    serializer_class = KnowledgeBaseSerializer

    def get_queryset(self):
        user = self.request.user
        user_skills = user.skills.all()
        return KnowledgeBase.objects.filter(
            skills__in=user_skills
        ).distinct()


class CourseViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели Course.
    """
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user
        user_specializations = user.specializations.all()
        return Course.objects.filter(
            specializations__in=user_specializations
        ).distinct()


class SpecializationViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели Specialization.
    """
    serializer_class = SpecializationSerializer
    queryset = Specialization.objects.all()

    @action(detail=True, methods=['post'])
    def add_spec(self, request, pk=None):
        """
        Выбор специальности.
        """
        specialization = self.get_object()
        user = request.user
        skills = specialization.skills.all()
        for skill in skills:
            user_skill, _ = UserSkill.objects.get_or_create(user=user,
                                                            skill=skill)
            user_skill.save()
        user.specializations.add(specialization)
        user.save()
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для теста.
    """
    queryset = QuestionTest.objects.all()
    serializer_class = QuestionTestSerializer

    @action(detail=False, methods=['post'])
    def take_test(self, request, *args, **kwargs):
        """
        Прохождение теста и обновление данных юзера.
        """
        user = self.request.user

        test_availability_response = is_test_available_for_user(request, user)

        if test_availability_response:
            return Response({'message': test_availability_response},
                            status=status.HTTP_400_BAD_REQUEST)
        specialization_id = request.data.get('specialization_id')
        if specialization_id:
            specialization = get_object_or_404(Specialization,
                                               id=specialization_id)
            skills = specialization.skills.all()
            answers_data = request.data.get('answers', [])
            total_points_by_skill = {skill: 0 for skill in skills}
            for answer_data in answers_data:
                question_id = answer_data.get('id_question')
                answers = answer_data.get('id_answer', [])
                question = get_object_or_404(QuestionTest, id=question_id)
                # Проверяем, что вопрос соответствует специализации
                question_skill = question.skills
                if question_skill not in skills:
                    return Response({'error': 'Вопрос не соответствует'
                                     'специальности'},
                                    status=status.HTTP_400_BAD_REQUEST)
                for answer in answers:
                    answer_id = answer.get('id')
                    answer_obj = get_object_or_404(AnswerTest, id=answer_id)

                    # Обновляем баллы по навыку
                    total_points_by_skill.setdefault(question_skill, 0)
                    total_points_by_skill[question_skill] += (
                        answer_obj.get_float_point_answer()
                    )
            # Обновление уровней навыков пользователя и их подсчет
            for skill, total_points in total_points_by_skill.items():
                self.calculate_skill_level(total_points)
                self.update_user_skills(user, skill, total_points)

            # Обновление информации о грейде после обновления навыков
            grade_info = self.update_user_grade(user)

            # Обновление даты прохождения теста и даты следующей сдачи
            user.test_date = timezone.now()
            unavailable_period = timedelta(days=14)
            user.next_test_date = (user.test_date + unavailable_period)
            user.save()

        return Response({'grade_info': grade_info})

    def update_user_skills(self, user, skill, total_points):
        """
        Обновление уровня навыков юзера.
        """
        user_skill, _ = UserSkill.objects.get_or_create(user=user,
                                                        skill=skill)
        skill_level = self.calculate_skill_level(total_points)
        user_skill.level = skill_level
        user_skill.save()

    def calculate_skill_level(self, total_points):
        """
        Подсчет уровня навыков.
        """
        if 0 <= total_points < 3:
            return 1
        if 3.25 <= total_points < 6.75:
            return 2
        if total_points >= 7:
            return 3
        return 0

    def update_user_grade(self, user):
        """
        Обновление грейда юзера, подсчет общего количества навыков юзера и
        необходимых навыков для улучшения.
        """
        user.grades.clear()
        user_skills = UserSkill.objects.filter(user=user)
        junior_grade = Grade.objects.get(title=settings.JUNIOR_GRADE)
        middle_grade = Grade.objects.get(title=settings.MIDLE_GRADE)
        senior_grade = Grade.objects.get(title=settings.SENIOR_GRADE)

        skills_max = user_skills.count()
        if any(user_skill.level == 1 for user_skill in user_skills):
            user.grades.add(junior_grade)
            next_grade = middle_grade
        elif all(user_skill.level >= 2 for user_skill in user_skills):
            user.grades.add(middle_grade)
            next_grade = senior_grade
        elif all(user_skill.level == 3 for user_skill in user_skills):
            user.grades.add(senior_grade)
            next_grade = None

        grade = user.grades.first().title
        if grade == settings.JUNIOR_GRADE:
            skills_current = sum(
                1 for skill in user_skills if skill.level == 1
            )
        if grade == settings.MIDLE_GRADE:
            skills_current = sum(
                1 for skill in user_skills if skill.level == 2
            )
        else:
            skills_current = None

        return {
            'grade_current': (
                user.grades.first().title if user.grades.first() else None
            ),
            'next_grade': next_grade.title if next_grade else None,
            'skills_current': skills_current,
            'skills_max': skills_max
        }

    @action(detail=False, methods=['get'])
    def get_questions_by_specialization(self, request):
        """
        Получение вопросов по определенной специализации.
        """
        specialization_id = request.query_params.get('specialization_id')
        if specialization_id:
            specialization = get_object_or_404(Specialization,
                                               id=specialization_id)
            skills = specialization.skills.all()
            questions = QuestionTest.objects.filter(skills__in=skills)
            serializer = self.get_serializer(questions, many=True)
            return Response(serializer.data)
        return Response({'error': 'Не указана специализация'},
                        status=status.HTTP_400_BAD_REQUEST)
