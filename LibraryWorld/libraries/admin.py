from django.contrib import admin

from .models import Book, Library


# Register your models here.

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address']
    list_filter = ['name']
    list_display_links = ['id', 'name', 'address']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'genre', 'publication_date', 'description']
    list_filter = ['author', 'genre']
    list_display_links = ['id','author', 'title']
