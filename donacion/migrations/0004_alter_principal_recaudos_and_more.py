# Generated by Django 4.2.3 on 2023-08-01 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donacion', '0003_alter_principal_recaudos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='recaudos',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='principal',
            name='total_donativos',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='salud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('valor_donado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_donacion', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donacion.principal')),
            ],
            options={
                'db_table': 'cruz_roja_en_accion',
            },
        ),
        migrations.CreateModel(
            name='humanitaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('valor_donado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_donacion', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donacion.principal')),
            ],
            options={
                'db_table': 'recoleccion_de_alimentos',
            },
        ),
        migrations.CreateModel(
            name='educacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('valor_donado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_donacion', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donacion.principal')),
            ],
            options={
                'db_table': 'educando_a_lo_lejos',
            },
        ),
        migrations.CreateModel(
            name='animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('valor_donado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_donacion', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donacion.principal')),
            ],
            options={
                'db_table': 'mi_pet',
            },
        ),
    ]
