from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    """
    Определиние базового менеджера моделей для пользовательской модели.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Создание и сохранение пользователя с указанным адресом электронной
        почты и паролем.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Создание и сохранение суперпользователя с указанным адресом электронной
        почты и паролем.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Кастомная модель пользователя.
    """
    username = None
    email = models.EmailField(
        'Почта',
        max_length=150,
        blank=False,
        unique=True
    )
    first_name = models.CharField('Имя', max_length=150, blank=False)
    last_name = models.CharField('Фамилия', max_length=150, blank=False)
    skills = models.ManyToManyField(
        'career_toolbox.Skill',
        related_name='user_skills',
        verbose_name='Навыки пользователя'
    )
    grades = models.ManyToManyField(
        'career_toolbox.Grade',
        related_name='user_grades',
        verbose_name='Грейды пользователя'
    )
    specializations = models.ManyToManyField(
        'career_toolbox.Specialization',
        related_name='user_specializations',
        verbose_name='Специализации пользователя'
    )
    course = models.ManyToManyField(
        'career_toolbox.Course',
        related_name='user_course',
        verbose_name='Курсы пользователя'
    )
    last_evaluation_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата последней оценки'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['id', ]

    def __str__(self):
        return self.email
