# Generated by Django 4.0.3 on 2022-03-07 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mas_problem', '0004_alter_problem_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='level',
        ),
    ]
