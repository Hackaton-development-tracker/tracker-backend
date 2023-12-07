from django.db import models


class Test(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название теста'
    )
    skill = models.ForeignKey(
        'career_toolbox.Skill',
        on_delete=models.SET_NULL,
        verbose_name='Навык для тестирования',
        related_name='test_skill',
        null=True
    )

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField(
        verbose_name='Текст вопроса'
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        verbose_name='Тест',
        related_name='questions'
    )

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(
        max_length=255,
        verbose_name='Текст ответа'
    )
    points = models.IntegerField(
        verbose_name='Баллы за ответ'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Вопрос',
        related_name='answers'
    )

    def __str__(self):
        return self.text
