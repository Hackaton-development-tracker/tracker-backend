from career_toolbox.models import Specialization
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.serializers import *
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
            user_skill, created = UserSkill.objects.get_or_create(user=user, skill=skill)
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
            specialization = get_object_or_404(Specialization, id=specialization_id)
            skills = specialization.skills.all()
            questions = QuestionTest.objects.filter(skills__in=skills)

            answers_data = request.data.get('answers', [])
            total_points = 0

            for answer_data in answers_data:
                question_id = answer_data.get('id_question')
                question = get_object_or_404(QuestionTest, id=question_id)

                if question in questions:
                    if isinstance(answer_data.get('id_answer'), list):
                        for answer in answer_data.get('id_answer', []):
                            answer_id = answer.get('id')
                            answer_obj = get_object_or_404(AnswerTest, id=answer_id)
                            total_points += answer_obj.get_float_point_answer()
                    else:
                        return Response({'error': 'Формат ответа не является списком'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'Вопрос не соответствует специальности'}, status=status.HTTP_400_BAD_REQUEST)

            # Обновление уровня навыков пользователя
            skill_level = self.calculate_skill_level(total_points)
            user = self.request.user

            # Получаем все навыки пользователя в данной специализации через связь UserSkill
            user_skills = UserSkill.objects.filter(user=user, skill__in=skills)

            for user_skill in user_skills:
                user_skill.level = skill_level
                user_skill.save()

            return Response({'message': 'Ответы успешно обработаны!', 'total_points': total_points, 'skill_level': skill_level})
        else:
            return Response({'error': 'Не указана специальность'}, status=status.HTTP_400_BAD_REQUEST)


    def update_user_skills(self, user, skill_level, specialization=None):
        # Обновляем уровень навыков пользователя для всех навыков или навыков в указанной специализации
        if specialization:
            skills_to_update = user.skills.filter(specialization=specialization)
        else:
            skills_to_update = user.skills.all()

        for skill in skills_to_update:
            user_skill, created = UserSkill.objects.get_or_create(
                user=user,
                skill=skill
            )

            user_skill.level = skill_level
            user_skill.save()

    def calculate_skill_level(self, total_points):
        if 0 <= total_points <= 6:
            return 1
        elif 6 < total_points <= 9:
            return 2
        elif total_points > 9:
            return 3
        else:
            return 0

    @action(detail=False, methods=['get'])
    def get_questions_by_specialization(self, request):
        specialization_id = request.query_params.get('specialization_id')

        if specialization_id:
            specialization = get_object_or_404(Specialization, id=specialization_id)
            skills = specialization.skills.all()
            questions = QuestionTest.objects.filter(skills__in=skills)
            serializer = self.get_serializer(questions, many=True)
            serializer = self.get_serializer(questions, many=True)
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Не указана специализация'}, status=status.HTTP_400_BAD_REQUEST)