# Generated by Django 5.1 on 2024-08-27 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("social_app", "0004_customuser_friends"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="friends",
        ),
    ]
