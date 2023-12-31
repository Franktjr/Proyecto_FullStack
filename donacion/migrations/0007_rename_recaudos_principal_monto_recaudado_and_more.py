# Generated by Django 4.2.3 on 2023-08-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donacion', '0006_alter_principal_recaudos_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='principal',
            old_name='recaudos',
            new_name='monto_recaudado',
        ),
        migrations.AddField(
            model_name='principal',
            name='beneficiario',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='principal',
            name='descripcion',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='principal',
            name='fecha_cierre',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='principal',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='principal',
            name='monto_a_recuadar',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
