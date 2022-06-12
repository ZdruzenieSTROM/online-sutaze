# Generated by Django 4.0 on 2022-06-11 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start', models.DateTimeField(verbose_name='Začiatok hry')),
                ('end', models.DateTimeField(verbose_name='Koniec hry')),
            ],
            options={
                'verbose_name': 'šifrovačka',
            },
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.CharField(max_length=100, verbose_name='Riešenie')),
                ('file', models.FileField(upload_to='', verbose_name='Zadanie')),
                ('pdf_solution', models.FileField(upload_to='', verbose_name='Riešnie v PDF')),
                ('level', models.PositiveIntegerField(verbose_name='Úroveň/Poradie')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kos.game')),
            ],
            options={
                'verbose_name': 'šifra',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('current_level', models.PositiveIntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kos.game')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competitor_answer', models.CharField(max_length=100)),
                ('submited_at', models.DateTimeField()),
                ('correct', models.BooleanField()),
                ('puzzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kos.puzzle')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kos.team')),
            ],
        ),
    ]