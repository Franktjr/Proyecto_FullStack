# Generated by Django 4.2.3 on 2023-08-01 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donacion', '0004_alter_principal_recaudos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='recaudos',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='principal',
            name='total_donativos',
            field=models.CharField(max_length=50),
        ),
    ]
