# Generated by Django 5.0 on 2023-12-21 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marcador_Byte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='empleado_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID Empleado'),
        ),
    ]