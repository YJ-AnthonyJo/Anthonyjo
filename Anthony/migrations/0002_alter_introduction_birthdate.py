# Generated by Django 3.2.7 on 2021-09-10 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anthony', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduction',
            name='birthdate',
            field=models.DateField(),
        ),
    ]
