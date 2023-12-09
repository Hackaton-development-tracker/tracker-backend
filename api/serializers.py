from career_toolbox.models import *
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from users.models import User
from quiz.models import *


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



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class AnswerTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerTest
        fields = ['id', 'answer']

class QuestionTestSerializer(serializers.ModelSerializer):
    answers = AnswerTestSerializer(many=True, source='answertest_questions', read_only=True)

    class Meta:
        model = QuestionTest
        fields = ['id', 'question', 'answers']


class TakeTestSerializer(serializers.Serializer):
    answers = AnswerTestSerializer(many=True)