# Generated by Django 4.2.7 on 2023-12-07 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('career_toolbox', '0002_initial'),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={},
        ),
        migrations.RemoveField(
            model_name='test',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='test',
            name='test_content',
        ),
        migrations.AddField(
            model_name='test',
            name='skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_skill', to='career_toolbox.skill', verbose_name='Навык для тестирования'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.test', verbose_name='Тест')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Текст ответа')),
                ('points', models.IntegerField(verbose_name='Баллы за ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz.question', verbose_name='Вопрос')),
            ],
        ),
    ]
