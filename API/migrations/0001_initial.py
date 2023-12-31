# Generated by Django 4.1.13 on 2023-12-06 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDSensor', models.CharField(max_length=20)),
                ('nivelContaminacion', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('latitud', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('longitud', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('fechaRegistro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
