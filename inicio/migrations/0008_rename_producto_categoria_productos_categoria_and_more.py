# Generated by Django 4.2.6 on 2023-11-15 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_alter_proveedor_proveedor_mail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='producto_categoria',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='producto_descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='producto_fecha',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='producto_imagen',
            new_name='imagen',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='producto_nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='producto_precio',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='producto_stock',
            new_name='stock',
        ),
    ]
