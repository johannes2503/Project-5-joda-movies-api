# Generated by Django 4.2.2 on 2023-06-13 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="review",
            field=models.TextField(default="", max_length=360),
        ),
    ]