# Generated by Django 4.0 on 2021-12-31 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=128)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('registration_start', models.DateTimeField()),
                ('registration_end', models.DateTimeField()),
                ('max_session_duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verbose_name', models.CharField(max_length=50)),
                ('shortcut', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('solution', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competitor_answer', models.FloatField()),
                ('submited_at', models.DateTimeField()),
                ('correct', models.BooleanField()),
                ('competitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mas_problem.competitor')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mas_problem.problem')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('min_solved_to_unlock', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mas_problem.game')),
                ('is_starting_level_for_grades', models.ManyToManyField(to='mas_problem.Grade')),
                ('previous_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mas_problem.level')),
            ],
        ),
        migrations.AddField(
            model_name='competitor',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mas_problem.grade'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user'),
        ),
    ]
