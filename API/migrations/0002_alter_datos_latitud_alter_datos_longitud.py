# Generated by Django 4.1.13 on 2023-12-06 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='latitud',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='datos',
            name='longitud',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=10),
        ),
    ]
