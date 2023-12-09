from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from users.models import User
from career_toolbox.models import (Specialization, Grade, Skill)
from quiz.models import (Test, Question, Answer)


class SpecializationSerializer(serializers.ModelSerializer):
    """Сериализатор специальностей."""

    class Meta:
        model = Specialization
        fields = ('id', 'title')


class CustomUserSerializer(UserSerializer):
    """Cериализатор для получения юзера."""
    specializations = SpecializationSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'specializations')


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'title', 'point')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'points')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'text', 'answers')


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ('id', 'title', 'skill', 'questions')


class SkillSerializer(serializers.ModelSerializer):
    tests = TestSerializer(many=True)

    class Meta:
        model = Skill
        fields = ('id', 'title', 'description', 'level', 'rating', 'tests')


class SpecializationDetailSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)

    class Meta:
        model = Specialization
        fields = ('id', 'title', 'description', 'skills')
