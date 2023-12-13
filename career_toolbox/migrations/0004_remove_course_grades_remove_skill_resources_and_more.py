# Generated by Django 4.2.7 on 2023-12-12 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('career_toolbox', '0003_remove_skill_description_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='grades',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='resources',
        ),
        migrations.RemoveField(
            model_name='specialization',
            name='knowledgebase',
        ),
        migrations.RemoveField(
            model_name='course',
            name='specializations',
        ),
        migrations.AlterField(
            model_name='project',
            name='external_resources',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resourse_projects', to='career_toolbox.externalresource', verbose_name='Ссылки на внешние ресурсы'),
        ),
        migrations.AddField(
            model_name='course',
            name='specializations',
            field=models.ManyToManyField(null=True, related_name='course_specialization', to='career_toolbox.specialization', verbose_name='Специальности'),
        ),
    ]
