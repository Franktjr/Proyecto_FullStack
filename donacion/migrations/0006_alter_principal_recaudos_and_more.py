# Generated by Django 4.2.3 on 2023-08-01 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donacion', '0005_alter_principal_recaudos_and_more'),
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
    ]