# Generated by Django 4.1.4 on 2022-12-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="Назва")),
                (
                    "subtitle",
                    models.CharField(max_length=250, verbose_name="Підзаголовок"),
                ),
                ("author", models.CharField(max_length=100, verbose_name="Автор")),
                ("isbn", models.CharField(max_length=13)),
            ],
        ),
    ]
