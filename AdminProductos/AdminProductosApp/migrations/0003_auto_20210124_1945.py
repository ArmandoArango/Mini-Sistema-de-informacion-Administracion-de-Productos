# Generated by Django 3.1.5 on 2021-01-25 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminProductosApp', '0002_auto_20210124_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='apellidos',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='cedula',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
