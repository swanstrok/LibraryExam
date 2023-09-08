from django.db import models


# Create your models here.
class Book(models.Model):
    """Модель книги"""
    title = models.CharField(max_length=80, verbose_name='Название')
    author = models.CharField(max_length=200, verbose_name='Автор')
    genre = models.CharField(max_length=80, verbose_name='Жанр')
    publication_date = models.DateField(verbose_name='Дата публикации')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Library(models.Model):
    """Модель библиотеки"""
    name = models.CharField(max_length=80, verbose_name='Название')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    books = models.ManyToManyField(to='Book', related_name='books')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотеки'
