from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','price','added_at','discount')
    list_filter = ('title','author','added_at')
