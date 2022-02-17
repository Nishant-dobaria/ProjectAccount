# Generated by Django 4.0.1 on 2022-02-17 03:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_alter_project_project_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['project_date_time']},
        ),
        migrations.AddField(
            model_name='project',
            name='project_date_time',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
