# Generated by Django 4.2.6 on 2023-11-15 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosextra',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='datosextra',
            name='fecha_de_nacimiento',
        ),
        migrations.RemoveField(
            model_name='datosextra',
            name='nombre_y_apellido',
        ),
        migrations.RemoveField(
            model_name='datosextra',
            name='user',
        ),
    ]
