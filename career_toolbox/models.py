from django.db import models


class Project(models.Model):
    """Таблица с проектами пользователей."""

    title = models.CharField(
        max_length=255,
        verbose_name='Название проекта'
    )
    description = models.TextField(
        verbose_name='Описание проекта'
    )
    start_date = models.DateField(
        verbose_name='Дата старта проекта'
    )
    end_date = models.DateField(
        verbose_name='Дата окончания проекта',
        null=True,
        blank=True
    )
    external_resources = models.ForeignKey(
        'career_toolbox.ExternalResource',
        on_delete=models.CASCADE,
        verbose_name='Ссылки на внешние ресурсы',
        related_name='resourse_projects'
    )
    specializations = models.ForeignKey(
        'career_toolbox.Specialization',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Специализации',
        related_name='project_specializtion'
    )
    users = models.ManyToManyField(
        'users.User',
        verbose_name='Пользователи',
        related_name='projects_user'
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class ExternalResource(models.Model):
    """Таблица с внешними ресурсами."""

    title = models.CharField(
        max_length=255,
        verbose_name='Название внешнего ресурса'
    )
    description = models.TextField(
        verbose_name='Описание ресурса'
    )
    url = models.URLField(
        verbose_name='URL ресурса'
    )
    courses = models.ManyToManyField(
        'career_toolbox.Course',
        verbose_name='Курсы пользователей, размещенные на ресурсе'
    )
    projects = models.ManyToManyField(
        'career_toolbox.Project',
        verbose_name='Проекты, связанные с ресурсом',
        related_name='projects_resourse'
    )

    class Meta:
        verbose_name = 'Внешний ресурс'
        verbose_name_plural = 'Внешние ресурсы'

    def __str__(self):
        return self.title


class Course(models.Model):
    """Таблица с курсами пользователей."""

    title = models.CharField(
        max_length=255,
        verbose_name='Название курса'
    )
    description = models.TextField(
        verbose_name='Описание курса'
    )
    start_date = models.DateField(
        verbose_name='Дата начала обучения'
    )
    end_date = models.DateField(
        verbose_name='Дата окончания обучения',
        null=True,
        blank=True
    )
    external_resources = models.ForeignKey(
        'career_toolbox.ExternalResource',
        on_delete=models.CASCADE,
        verbose_name='Ссылки на внешние ресурсы'
    )
    specializations = models.ForeignKey(
        'career_toolbox.Specialization',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Специальности',
        related_name='course_specialization'
    )
    grades = models.ForeignKey(
        'career_toolbox.Grade',
        on_delete=models.CASCADE,
        verbose_name='Грейды',
        related_name='course_grade'
    )
    users = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователи',
        related_name='courses_user'
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title


class Specialization(models.Model):
    """Таблица со специальностями."""

    title = models.CharField(
        max_length=255,
        verbose_name="Название специальности"
    )
    description = models.TextField(
        verbose_name='Описание специальности'
    )
    grades = models.ForeignKey(
        'career_toolbox.Grade',
        on_delete=models.CASCADE,
        verbose_name='Грейды',
        related_name='courses_grade'
    )
    skills = models.ManyToManyField(
        'career_toolbox.Skill',
        verbose_name='Навыки по специализациям',
        related_name='specialization_skulls'
    )
    users = models.ManyToManyField(
        'users.User',
        related_name='specializations_users',
        verbose_name='Специализации пользователей'
    )

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return self.title


class Grade(models.Model):
    """Таблица с грейдами."""

    title = models.CharField(
        max_length=255,
        verbose_name='Название грейда'
    )
    point = models.IntegerField(
        verbose_name='Балл'
    )
    specializations = models.ForeignKey(
        'career_toolbox.Specialization',
        on_delete=models.CASCADE,
        verbose_name='Специальности',
        related_name='grade_specialization'
    )
    сourses = models.ForeignKey(
        'career_toolbox.Course',
        on_delete=models.CASCADE,
        verbose_name='Курсы',
        related_name='grade_course'
    )
    users = models.ManyToManyField(
        'users.User',
        verbose_name='Грейды пользователей',
        related_name='grade_users'
    )

    class Meta:
        verbose_name = 'Грейд'
        verbose_name_plural = 'Грейды'

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название навыка'
    )
    description = models.TextField(
        verbose_name='Описание навыка'
    )
    specializations = models.ManyToManyField(
        'career_toolbox.Specialization',
        verbose_name='Специальности',
        related_name='skill_specializations'
    )
    resources = models.ForeignKey(
        'career_toolbox.ExternalResource',
        on_delete=models.CASCADE,
        verbose_name='Ссылки на внешние ресурсы',
        null=True
    )
    level = models.CharField(
        max_length=255,
        verbose_name='Уровень'
    )
    rating = models.IntegerField(
        verbose_name='Оценка'
    )
    tests = models.OneToOneField(
        'quiz.Test',
        on_delete=models.SET_NULL,
        verbose_name='Тесты по специализации',
        related_name='skill_test',
        null=True
    )
    users = models.ManyToManyField(
        'users.User',
        related_name='skill_users',
        verbose_name='Специализации пользователей'
    )

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.title
