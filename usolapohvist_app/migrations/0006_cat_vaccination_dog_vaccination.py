# Generated by Django 5.0.6 on 2024-06-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usolapohvist_app", "0005_cat_sterilization_dog_sterilization_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cat",
            name="vaccination",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="dog",
            name="vaccination",
            field=models.BooleanField(default=False),
        ),
    ]
