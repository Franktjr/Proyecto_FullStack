# Generated by Django 4.2.3 on 2023-09-01 02:26

from django.db import migrations, models
import django.db.models.deletion
import donacion.models


class Migration(migrations.Migration):

    dependencies = [
        ('donacion', '0021_alter_campania_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='SOLICITUDES_CAMPANIAS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('nombre_campania', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=5000)),
                ('beneficiario', models.CharField(max_length=200)),
                ('monto_a_recaudar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('direccion', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=500)),
                ('categoria', models.ForeignKey(default=donacion.models.categoria_alterna, on_delete=django.db.models.deletion.SET_DEFAULT, to='donacion.categorias')),
            ],
        ),
    ]
