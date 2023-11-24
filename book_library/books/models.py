from django.db import models


class Book(models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Название книги'
    )
    author = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Имя автора'
    )
    publishing_year = models.PositiveSmallIntegerField()(
        verbose_name='Год издания'
    )
    isbn = models.CharField(
        max_length=13,
        unique=True,
        verbose_name='ISBN'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return (self.name)
