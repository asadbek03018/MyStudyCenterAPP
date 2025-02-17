# Generated by Django 5.1.1 on 2024-09-26 06:49

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
        ('study_center', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='fanlar',
            field=models.ManyToManyField(blank=True, related_name='accounts', to='study_center.fanlar'),
        ),
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='account_groups', to='study_center.group'),
        ),
        migrations.CreateModel(
            name='HistoricalAccount',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_id', models.CharField(blank=True, db_index=True, editable=False, max_length=10, null=True)),
                ('username', models.CharField(db_index=True, max_length=50)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=80, null=True)),
                ('phone', models.CharField(max_length=50)),
                ('profile_image', models.TextField(blank=True, max_length=100, null=True)),
                ('total_score', models.FloatField(blank=True, default=0, null=True)),
                ('month_score', models.FloatField(blank=True, default=0, null=True)),
                ('telegram_user_id', models.IntegerField(blank=True, null=True)),
                ('phone_home', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.CharField(choices=[('director', 'director'), ('teacher', 'teacher'), ('student', 'student')], max_length=29)),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('last_payment_date', models.DateTimeField(blank=True, null=True)),
                ('is_grand', models.BooleanField(blank=True, default=False, null=True)),
                ('is_payed', models.BooleanField(blank=True, default=False, null=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(blank=True, editable=False)),
                ('last_login', models.DateTimeField(blank=True, editable=False)),
                ('is_leave', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_premium', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('study_center', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='study_center.studycenter')),
                ('studying', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='study_center.studycenter')),
            ],
            options={
                'verbose_name': 'historical account',
                'verbose_name_plural': 'historical accounts',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
