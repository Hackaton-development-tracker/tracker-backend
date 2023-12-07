# Generated by Django 4.2.7 on 2023-12-07 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('career_toolbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название теста')),
                ('test_content', models.TextField(verbose_name='Тест')),
                ('skills', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_skill', to='career_toolbox.skill', verbose_name='Навык для тестирования')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
    ]
