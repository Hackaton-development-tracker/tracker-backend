# Generated by Django 4.2.7 on 2023-12-12 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('career_toolbox', '0003_remove_skill_description_level'),
        ('quiz', '0005_questiontest_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questiontest',
            name='skills',
        ),
        migrations.AddField(
            model_name='questiontest',
            name='skills',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_skill', to='career_toolbox.skill', verbose_name='Навык для тестирования'),
        ),
    ]
