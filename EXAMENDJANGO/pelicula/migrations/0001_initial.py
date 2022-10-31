# Generated by Django 4.1.2 on 2022-10-31 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('año', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Copias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_copias', models.IntegerField()),
                ('formato', models.CharField(max_length=255)),
                ('pelicula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pelicula.pelicula')),
            ],
        ),
    ]