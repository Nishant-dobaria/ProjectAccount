# Generated by Django 4.0.1 on 2022-02-17 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_project_options_project_project_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]