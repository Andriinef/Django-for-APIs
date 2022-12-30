from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField("Ім'я", null=True, blank=True, max_length=100)
    age = models.PositiveIntegerField(
        "Вік", null=True, blank=True, help_text="Вкажить свій вік."
    )

    class Meta:
        verbose_name = "Акаунт"
        verbose_name_plural = "Акаунти"
