# Generated by Django 4.2.7 on 2023-12-01 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('career_toolbox', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'База знаний',
                'verbose_name_plural': 'Базы знаний',
            },
        ),
        migrations.RemoveField(
            model_name='course',
            name='users',
        ),
        migrations.RemoveField(
            model_name='project',
            name='users',
        ),
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(max_length=255, verbose_name='Уровень навыка'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='rating',
            field=models.IntegerField(verbose_name='Оценка навыка'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='specializations',
            field=models.ManyToManyField(related_name='skill_specializations', to='career_toolbox.specialization', verbose_name='Навыки по специальностям'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='tests',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skill_test', to='quiz.test', verbose_name='Тесты по навыкам специализации'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='users',
            field=models.ManyToManyField(related_name='skill_users', to=settings.AUTH_USER_MODEL, verbose_name='Навыки пользователей'),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='grades',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialization_grade', to='career_toolbox.grade', verbose_name='Грейды'),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='skills',
            field=models.ManyToManyField(related_name='specialization_skills', to='career_toolbox.skill', verbose_name='Навыки по специализациям'),
        ),
        migrations.AddField(
            model_name='specialization',
            name='knowledgebase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialization_base', to='career_toolbox.knowledgebase', verbose_name='База знаний по специальности'),
        ),
    ]
