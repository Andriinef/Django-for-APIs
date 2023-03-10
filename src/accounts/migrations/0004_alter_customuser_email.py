# Generated by Django 4.1.4 on 2022-12-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_customuser_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
    ]
