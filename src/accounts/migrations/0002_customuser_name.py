# Generated by Django 4.1.4 on 2022-12-29 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Ім'я"
            ),
        ),
    ]
