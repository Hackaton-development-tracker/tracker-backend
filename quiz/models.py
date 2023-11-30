from django.db import models


class Test(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название теста'
    )
    test_content = models.TextField(
        verbose_name='Тест'
    )
    skills = models.OneToOneField(
        'career_toolbox.Skill',
        on_delete=models.SET_NULL,
        verbose_name='Навык для тестирования',
        related_name='test_skill',
        null=True
    )

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.title
