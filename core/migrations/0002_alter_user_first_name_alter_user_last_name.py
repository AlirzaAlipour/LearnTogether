# Generated by Django 5.0.7 on 2024-07-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=30),
        ),
    ]
