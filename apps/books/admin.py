from django.contrib import admin
from .models import Book,Review

class ReviewInline(admin.TabularInline):
    model = Review
    exclude = ('likes',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','price','added_at','discount')
    list_filter = ('title','author','added_at')

    inlines = [
        ReviewInline,
    ]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book','review','author','count_likes')
    list_filter = ('book','review','author')
    exclude = ('likes',)

    def count_likes(self,obj):
        return str(obj.likes.count())