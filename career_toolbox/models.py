from django.db import models


class Project(models.Model):
    """Таблица с проектами."""

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
    specializations = models.ManyToManyField(
        'career_toolbox.Specialization',
        verbose_name='Специализации',
        related_name='project_specializtion'
    )
    file = models.FileField(
        upload_to='projects/',
        verbose_name='Файл'
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

    class Meta:
        verbose_name = 'Внешний ресурс'
        verbose_name_plural = 'Внешние ресурсы'

    def __str__(self):
        return self.title


class Course(models.Model):
    """Таблица с курсами."""

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
    specializations = models.ManyToManyField(
        'career_toolbox.Specialization',
        verbose_name='Специальности',
        related_name='course_specialization'
    )
    resource = models.ForeignKey(
        'career_toolbox.ExternalResource',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Внешний ресурс где размещен курс',
        blank=True
    )
    file = models.FileField(
        upload_to='courses/',
        verbose_name='Файл'
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
    skills = models.ManyToManyField(
        'career_toolbox.Skill',
        verbose_name='Навыки по специализациям',
        related_name='specialization_skills'
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
    description = models.TextField(
        verbose_name='Описание'
    )
    point = models.IntegerField(
        verbose_name='Балл'
    )

    class Meta:
        verbose_name = 'Грейд'
        verbose_name_plural = 'Грейды'

    def __str__(self):
        return self.title


class Level(models.Model):
    """Таблица с уровнями для навыков."""
    level = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Уровень навыка'
    )
    description_level = models.TextField(
        verbose_name='Описание навыка'
    )

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

    def __str__(self):
        return str(self.level)


class Skill(models.Model):
    """Таблица с навыками."""

    title = models.CharField(
        max_length=255,
        verbose_name='Название навыка'
    )
    description = models.TextField(
        verbose_name='Описание навыка'
    )
    tests = models.ManyToManyField(
        'quiz.QuestionTest',
        verbose_name='Тесты по навыкам специализации',
        related_name='skill_test',
        blank=True
    )
    base = models.ManyToManyField(
        'career_toolbox.KnowledgeBase',
        related_name='skill_knowledgebase',
        verbose_name='Документы из базы знаний',
        blank=True
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.SET_NULL,
        verbose_name='Уровень навыка',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Таблица с тегами."""
    name = models.CharField(
        max_length=255,
        verbose_name='Название тега'
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class KnowledgeBase(models.Model):
    """Таблица с базой знаний."""

    theme = models.CharField(
        max_length=255,
        verbose_name='Тема'
    )
    type = models.CharField(
        max_length=150,
        verbose_name='Тип'
    )
    tags = models.ManyToManyField(
        'career_toolbox.Tag',
        related_name='knowledgebase_tags',
        verbose_name='Теги'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    author = models.CharField(
        max_length=255,
        verbose_name='Автор',
    )
    skills = models.ManyToManyField(
        'career_toolbox.Skill',
        related_name='knowledgebase_skills',
        verbose_name='База по навыкам',
    )

    class Meta:
        verbose_name = 'База знаний'
        verbose_name_plural = 'Базы знаний'

    def __str__(self):
        return self.theme
