# Generated by Django 3.2.15 on 2022-08-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_prority_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2022-07-07'),
            preserve_default=False,
        ),
    ]
