# Generated by Django 2.0.2 on 2018-09-28 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20180928_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='users_appeared',
        ),
    ]