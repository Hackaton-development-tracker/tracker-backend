from django.db import models


class QuestionTest(models.Model):
    """Таблица с вопросами."""
    QUESTION_TYPE_CHOICES = [
        ('one', 'Один вариант ответа'),
        ('several', 'Несколько вариантов ответа'),
    ]

    question = models.TextField(
        verbose_name='Вопрос'
    )
    skills = models.ForeignKey(
        'career_toolbox.Skill',
        on_delete=models.SET_NULL,
        verbose_name='Навык для тестирования',
        related_name='test_skill',
        null=True
    )
    param = models.CharField(
        max_length=10,
        choices=QUESTION_TYPE_CHOICES,
        verbose_name='Тип вопроса'
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question


class AnswerTest(models.Model):
    """Таблица с ответами на вопросы."""
    class PointsAnswerChoices(models.TextChoices):
        Variant_1 = 'V1', '0'
        Variant_2 = 'V2', '3'
        Variant_3 = 'V3', '1.5'
        Variant_4 = 'V4', '1'
        Variant_5 = 'V5', '0.75'

    questions = models.ForeignKey(
        'quiz.QuestionTest',
        on_delete=models.CASCADE,
        verbose_name='К вопросу',
        related_name='answertest_questions'
    )
    answer = models.TextField(
        verbose_name='Ответ'
    )
    point_answer = models.CharField(
        max_length=3,
        verbose_name='Баллы за ответ',
        choices=PointsAnswerChoices.choices,
        default=PointsAnswerChoices.Variant_1
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def get_float_point_answer(self):
        return float(dict(self.PointsAnswerChoices.choices)[self.point_answer])

    def __str__(self):
        return self.answer
