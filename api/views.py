from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import (CustomUserSerializer, QuestionTestSerializer,
                             SpecializationSerializer)
from career_toolbox.models import Grade, Specialization
from quiz.models import AnswerTest, QuestionTest
from users.models import User, UserSkill


class CustomUserViewSet(UserViewSet):
    """Вьюсет для модели User."""
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer


class SpecializationViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Specialization."""
    serializer_class = SpecializationSerializer
    queryset = Specialization.objects.all()

    @action(detail=True, methods=['post'])
    def add_spec(self, request, pk=None):
        """Выбор специальности."""
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
    queryset = QuestionTest.objects.all()
    serializer_class = QuestionTestSerializer

    @action(detail=False, methods=['post'])
    def take_test(self, request, *args, **kwargs):
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
            user = self.request.user
            skills_current = 0
            skills_max = 0
            for skill, total_points in total_points_by_skill.items():
                skill_level = self.calculate_skill_level(total_points)
                low_skills = self.count_skills(user, skill_level)
                if skill is not None:
                    skills_max += 1

                if low_skills > 0:
                    skills_current += 1
                self.update_user_skills(user, skill, total_points)
            total_points = sum(total_points_by_skill.values())
            grade_info = self.update_user_grade(user, total_points)
            return Response({'grade_info': grade_info,
                             'skills_current': skills_current,
                             'skills_max': skills_max})
        return Response({'error': 'Не указана специальность'},
                        status=status.HTTP_400_BAD_REQUEST)

    def update_user_skills(self, user, skill, total_points):
        user_skill, _ = UserSkill.objects.get_or_create(user=user,
                                                        skill=skill)
        skill_level = self.calculate_skill_level(total_points)
        user_skill.level = skill_level
        user_skill.save()

    def calculate_skill_level(self, total_points):
        if 0 <= total_points <= 6:
            return 1
        if 6 < total_points <= 9:
            return 2
        if total_points > 10:
            return 3
        return 0

    def count_skills(self, user, skill_level):
        skills_current = 0
        user_grade_level = user.grades.first().title.lower()
        if user_grade_level == 'junior' and skill_level == 1:
            skills_current += 1
        elif user_grade_level == 'middle' and skill_level < 2:
            skills_current += 1
        elif user_grade_level == 'senior' and skill_level < 3:
            skills_current += 1

        return skills_current

    def update_user_grade(self, user, total_points):
        user.grades.clear()
        # Находим грейд, соответствующий полученным баллам
        current_grade = Grade.objects.filter(
            point__lte=total_points).order_by('-point').first()
        next_grade = Grade.objects.filter(
            point__gte=total_points).order_by('point').first()
        if current_grade:
            user.grades.add(current_grade)
            return {
                'grade_current': (current_grade.title if current_grade
                                  else None),
                'grade_next': next_grade.title if next_grade else None
            }
        return Response({'error': 'Грейд пользователя остается без'
                         'изменений.'})

    @action(detail=False, methods=['get'])
    def get_questions_by_specialization(self, request):
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
