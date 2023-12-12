from django.conf import settings
from djoser.serializers import UserSerializer
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from career_toolbox.models import (Course, ExternalResource, Grade,
                                   KnowledgeBase, Level, Project, Skill,
                                   Specialization, Tag)
from quiz.models import AnswerTest, QuestionTest
from users.models import User, UserSkill


class ProjectSerializer(serializers.ModelSerializer):
    """
    Сериализатор проектов.
    """
    image = Base64ImageField()

    class Meta:
        model = Project
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """
    Сериализатор тегов.
    """

    class Meta:
        model = Tag
        fields = '__all__'


class KnowledgeBaseSerializer(serializers.ModelSerializer):
    """
    Сериализатор базы знаний.
    """
    tags = TagSerializer(many=True)

    class Meta:
        model = KnowledgeBase
        fields = '__all__'


class ExternalResourceSerializer(serializers.ModelSerializer):
    """
    Сериализатор ссылок на внешние ресурсы.
    """

    class Meta:
        model = ExternalResource
        fields = ('url',)


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор курсов.
    """
    resource = ExternalResourceSerializer()
    image = Base64ImageField()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'start_date', 'end_date',
                  'resource', 'image')


class SpecializationSerializer(serializers.ModelSerializer):
    """
    Сериализатор специальностей.
    """

    class Meta:
        model = Specialization
        fields = ('id', 'title')


class GradeSerializer(serializers.ModelSerializer):
    """
    Сериализатор грейдов.
    """

    class Meta:
        model = Grade
        fields = ('title', )


class CustomUserSerializer(UserSerializer):
    """
    Cериализатор для получения юзера.
    """
    specializations = SpecializationSerializer(many=True)
    grades = GradeSerializer(many=True)
    next_grade = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'specializations', 'grades', 'next_grade',
                  'test_date', 'next_test_date')

    def get_next_grade(self, user):
        current_grades = user.grades.all()

        last_added_grade = current_grades.last()

        if last_added_grade is None:
            next_grade_title = settings.JUNIOR_GRADE
        elif last_added_grade.title == settings.JUNIOR_GRADE:
            next_grade_title = settings.MIDLE_GRADE
        elif last_added_grade.title == settings.MIDLE_GRADE:
            next_grade_title = settings.SENIOR_GRADE
        else:
            return None

        next_grade = Grade.objects.get(title=next_grade_title)
        return GradeSerializer(next_grade).data


class LevelSerializer(serializers.ModelSerializer):
    """
    Сериализатор уровней.
    """

    class Meta:
        model = Level
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    """
    Сериализатор навыков.
    """

    class Meta:
        model = Skill
        fields = ('id', 'title', 'description')


class UserSkillSerializer(serializers.ModelSerializer):
    """Сериализатор специальностей."""
    skill = SkillSerializer()
    current_level = serializers.SerializerMethodField()
    target_level = serializers.SerializerMethodField()
    total_levels = serializers.SerializerMethodField()
    levels_description = serializers.SerializerMethodField()

    class Meta:
        model = UserSkill
        fields = ('id', 'skill', 'current_level', 'target_level',
                  'total_levels', 'levels_description')

    def get_current_level(self, obj):
        return obj.level if obj.level else None

    def get_target_level(self, obj):
        return obj.level + 1 if obj.level else None

    def get_total_levels(self, obj):
        return Level.objects.count()

    def get_levels_description(self, obj):
        return {
            str(level.level): level.description_level
            for level in Level.objects.all()
        }


class AnswerTestSerializer(serializers.ModelSerializer):
    """
    Сериализатор ответов на тест.
    """

    class Meta:
        model = AnswerTest
        fields = ['id', 'answer']


class QuestionTestSerializer(serializers.ModelSerializer):
    """
    Сериализатор вопросов.
    """
    answers = AnswerTestSerializer(many=True, source='answertest_questions',
                                   read_only=True)

    class Meta:
        model = QuestionTest
        fields = ['id', 'question',  'param', 'answers']


class TakeTestSerializer(serializers.Serializer):
    """
    Сериализатор теста.
    """
    answers = AnswerTestSerializer(many=True)
