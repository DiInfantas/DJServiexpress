# Generated by Django 4.1.12 on 2023-11-22 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HorasTomadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id_servicio', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre_servicio', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nom_usuario', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=60)),
            ],
        ),
    ]