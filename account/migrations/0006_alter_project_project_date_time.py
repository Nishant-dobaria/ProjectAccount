# Generated by Django 4.0.1 on 2022-02-17 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_project_project_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_date_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
