# Generated by Django 5.0.6 on 2024-06-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usolapohvist_app", "0009_alter_dog_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dog",
            name="category",
            field=models.CharField(
                choices=[("dog", "Dog"), ("cat", "Cat")], default="dog"
            ),
        ),
    ]
