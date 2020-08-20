# Generated by Django 3.0.8 on 2020-08-20 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_auto_20200820_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='carreras',
            fields=[
                ('idcarrera', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('nombrecorto', models.CharField(max_length=10)),
                ('fecha_fundacion', models.DateField()),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
    ]
