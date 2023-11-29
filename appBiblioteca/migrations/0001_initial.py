# Generated by Django 4.2.7 on 2023-11-29 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('biografia', models.TextField()),
                ('foto', models.ImageField(upload_to='fotoAutores/')),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=150)),
                ('sitioWeb', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=60)),
                ('editorial', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('genero', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=100)),
                ('resume', models.TextField()),
                ('disponibilidad', models.CharField(choices=[('D', 'Disponible'), ('P', 'Prestado'), ('R', 'Reservado')], max_length=50)),
                ('portada', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libro_prestado', models.CharField(max_length=100)),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion', models.DateField()),
                ('usuario_prestamo', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('D', 'Devuelto'), ('P', 'Prestado')], max_length=50)),
            ],
        ),
    ]