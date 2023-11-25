from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'publishing_year', 'isbn')
    search_fields = ('name', 'author',)
    list_filter = ('name', 'author',)
    empty_value_display = '-empty-'
