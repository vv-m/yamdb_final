from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'category',)
    search_fields = ('name',)
    list_filter = ('category',)
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'score', 'pub_date',)
    search_fields = ('name', 'text')
    list_filter = ('author', 'score', 'pub_date',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'pub_date',)
    search_fields = ('text',)
    list_filter = ('author',)
    empty_value_display = '-пусто-'


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role',)
    search_fields = ('name', 'first_name', 'last_name',)
    list_filter = ('role',)
    empty_value_display = '-пусто-'


admin.site.register(Title, TitlesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User, UserAdmin)
