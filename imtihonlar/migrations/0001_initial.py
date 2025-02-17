# Generated by Django 5.1.1 on 2024-09-26 06:49

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('study_center', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamFan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ball', models.FloatField()),
                ('study_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_center.studycenter')),
            ],
            options={
                'verbose_name': 'Imtihon Fanlari',
                'verbose_name_plural': 'Imtihon Fanlari',
                'ordering': ['-ball'],
            },
        ),
        migrations.CreateModel(
            name='Imtihonlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('exam_token', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('fans', models.ManyToManyField(to='imtihonlar.examfan')),
                ('students', models.ManyToManyField(related_name='student_exams', to=settings.AUTH_USER_MODEL)),
                ('study_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_center.studycenter')),
                ('teachers', models.ManyToManyField(related_name='teacher_exams', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Imtihonlar',
                'verbose_name_plural': 'Imtihonlar',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results', models.JSONField()),
                ('checker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checked_results', to=settings.AUTH_USER_MODEL)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imtihonlar.imtihonlar')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "O'quvchi Natijalari",
                'verbose_name_plural': "O'quvchi Natijalari",
            },
        ),
    ]
