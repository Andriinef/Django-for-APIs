from django.db import models


class Book(models.Model):
    title = models.CharField("Назва", max_length=250)
    subtitle = models.CharField("Підзаголовок", max_length=250)
    author = models.CharField("Автор", max_length=100)
    isbn = models.CharField("Уникальный номер книжного издания", max_length=13)

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title
