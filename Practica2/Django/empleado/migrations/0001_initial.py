# Generated by Django 4.1.2 on 2022-10-28 17:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('genero', models.CharField(max_length=1)),
                ('fecha_contratacion', models.DateField(default=datetime.date(2022, 10, 28))),
            ],
        ),
        migrations.CreateModel(
            name='JefeDepartamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(default=datetime.date(2022, 10, 28))),
                ('fecha_fin', models.DateField()),
                ('idDepartamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleado.departamento')),
                ('idEmpleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleado.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Dept_empl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(default=datetime.date(2022, 10, 28))),
                ('fecha_fin', models.DateField()),
                ('idDepartamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleado.departamento')),
                ('idEmpleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleado.empleado')),
            ],
        ),
    ]
