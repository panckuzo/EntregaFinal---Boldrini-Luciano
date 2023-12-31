# Generated by Django 4.2.6 on 2023-10-29 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('productos', models.TextField()),
                ('Telefono', models.IntegerField(max_length=30)),
                ('mail', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_cliente', models.IntegerField(max_length=30)),
                ('resena', models.TextField()),
                ('calificacion', models.IntegerField(max_length=2)),
            ],
        ),
    ]
