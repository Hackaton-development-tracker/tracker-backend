# Generated by Django 4.2.7 on 2023-12-07 19:58


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('career_toolbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('skills', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_skill', to='career_toolbox.skill', verbose_name='Навык для тестирования')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='AnswerTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('point_answer', models.CharField(choices=[('V1', '0'), ('V2', '3'), ('V3', '1.5'), ('V4', '1'), ('V5', '0.75')], default='V1', max_length=3, verbose_name='Баллы за ответ')),
                ('grade', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answertest_grade', to='career_toolbox.grade', verbose_name='Связанный грейд')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answertest_questions', to='quiz.questiontest', verbose_name='К вопросу')),
                ('specializtion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answertest_specialization', to='career_toolbox.specialization', verbose_name='Связанная специализация')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
