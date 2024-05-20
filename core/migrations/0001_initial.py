# Generated by Django 5.0.3 on 2024-03-13 21:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('class_quantity', models.PositiveIntegerField(default=0, verbose_name='Cantidad de clases')),
                ('teacher', models.ForeignKey(limit_choices_to={'groups__name': 'profesores'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Profesor')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('present', models.BooleanField(blank=True, default=False, null=True, verbose_name='Presente')),
                ('student', models.ForeignKey(limit_choices_to={'groups__name': 'estudiantes'}, on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to=settings.AUTH_USER_MODEL, verbose_name='Estudiante')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course', verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'Asistencia',
                'verbose_name_plural': 'Asistencias',
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_1', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 1')),
                ('mark_2', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 2')),
                ('mark_3', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota 3')),
                ('average', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Promedio')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course', verbose_name='Curso')),
                ('student', models.ForeignKey(limit_choices_to={'groups__name': 'estudiantes'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Nota',
                'verbose_name_plural': 'Notas',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, verbose_name='Alumno Regular')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course', verbose_name='Curso')),
                ('student', models.ForeignKey(limit_choices_to={'groups__name': 'estudiantes'}, on_delete=django.db.models.deletion.CASCADE, related_name='students_registration', to=settings.AUTH_USER_MODEL, verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Inscripcion',
                'verbose_name_plural': 'Inscripciones',
            },
        ),
    ]
