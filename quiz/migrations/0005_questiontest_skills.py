# Generated by Django 4.2.7 on 2023-12-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_toolbox', '0003_remove_skill_description_level'),
        ('quiz', '0004_remove_questiontest_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiontest',
            name='skills',
            field=models.ManyToManyField(null=True, related_name='test_skill', to='career_toolbox.skill', verbose_name='Навык для тестирования'),
        ),
    ]
