# Generated by Django 3.2.7 on 2021-09-10 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_votes1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='votes1',
        ),
    ]
