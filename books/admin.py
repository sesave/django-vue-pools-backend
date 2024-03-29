from django.contrib import admin
from django.utils.text import get_text_list

from .models import Author, Book, Category, PublishingCompany, Rating, Comment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(PublishingCompany)
class PCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'book_id', 'rating')
    search_fields = ('id', 'comment')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating')
    search_fields = ('id', 'rating')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'publishingCompany', 'category', 'author',
    )
    list_display_links = ('id', 'name',)
    list_filter = ('publishingCompany', 'category',)
    search_fields = ('id', 'name', 'author__name',)
    autocomplete_fields = ('author', 'publishingCompany', 'category')
