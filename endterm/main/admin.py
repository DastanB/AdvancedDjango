from django.contrib import admin
from main.models import Article, ArticleImage, Favourite


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'city',)
    

@admin.register(ArticleImage)
class ArticleImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'image',)

@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'user')