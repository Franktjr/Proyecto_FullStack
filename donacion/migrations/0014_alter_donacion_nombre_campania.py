# Generated by Django 4.2.3 on 2023-08-16 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donacion', '0013_alter_donacion_nombre_campania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='nombre_campania',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donacion.campania'),
        ),
    ]
