# Generated by Django 3.0.8 on 2020-08-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_carreras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreras',
            name='fecha_fundacion',
            field=models.CharField(max_length=20),
        ),
    ]
