# Generated by Django 4.2.6 on 2023-11-13 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_perfil_profile_delete_datosextra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
