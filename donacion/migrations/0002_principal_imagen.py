# Generated by Django 4.2.3 on 2023-07-31 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='principal',
            name='imagen',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
