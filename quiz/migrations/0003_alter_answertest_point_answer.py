# Generated by Django 4.2.7 on 2023-12-09 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_answertest_point_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertest',
            name='point_answer',
            field=models.CharField(choices=[('V1', '0'), ('V2', '3'), ('V3', '1.5'), ('V4', '1'), ('V5', '0.75')], default='V1', max_length=3, verbose_name='Баллы за ответ'),
        ),
    ]
