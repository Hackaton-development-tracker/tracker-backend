# Generated by Django 4.2.7 on 2023-12-07 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
        ('career_toolbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='specializations_users', to=settings.AUTH_USER_MODEL, verbose_name='Специализации пользователей'),
        ),
        migrations.AddField(
            model_name='skill',
            name='base',
            field=models.ManyToManyField(related_name='skill_knowledgebase', to='career_toolbox.knowledgebase', verbose_name='Документы из базы знаний'),
        ),
        migrations.AddField(
            model_name='skill',
            name='resources',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='career_toolbox.externalresource', verbose_name='Ссылки на внешние ресурсы'),
        ),
        migrations.AddField(
            model_name='skill',
            name='specializations',
            field=models.ManyToManyField(related_name='skill_specializations', to='career_toolbox.specialization', verbose_name='Навыки по специальностям'),
        ),
        migrations.AddField(
            model_name='skill',
            name='tests',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skill_test', to='quiz.questiontest', verbose_name='Тесты по навыкам специализации'),
        ),
        migrations.AddField(
            model_name='project',
            name='external_resources',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='resourse_projects', to='career_toolbox.externalresource', verbose_name='Ссылки на внешние ресурсы'),
        ),
        migrations.AddField(
            model_name='project',
            name='specializations',
            field=models.ManyToManyField(related_name='project_specializtion', to='career_toolbox.specialization', verbose_name='Специализации'),
        ),
        migrations.AddField(
            model_name='knowledgebase',
            name='skills',
            field=models.ManyToManyField(related_name='knowledgebase_skills', to='career_toolbox.skill', verbose_name='База по навыкам'),
        ),
        migrations.AddField(
            model_name='course',
            name='grades',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_grade', to='career_toolbox.grade', verbose_name='Грейды'),
        ),
        migrations.AddField(
            model_name='course',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='career_toolbox.externalresource', verbose_name='Внешний ресурс где размещен курс'),
        ),
        migrations.AddField(
            model_name='course',
            name='specializations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_specialization', to='career_toolbox.specialization', verbose_name='Специальности'),
        ),
    ]
