from django.db import models
from django.contrib.auth.models import User
from main.constants import COLOR_BLUE, COLOR_GREEN, COLOR_RED, COLOR_WHITE, COLOR_TYPES
from utils.upload import article_delete_path, article_image_delete_path, article_image_path
from utils.validators import article_image_extension, article_image_size

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    price = models.PositiveIntegerField()
    city = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    color = models.PositiveSmallIntegerField(choices=COLOR_TYPES, default=COLOR_WHITE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.name

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to=article_image_path, validators=[article_image_size, article_image_extension],
                                null=True, blank=True)

    def __str__(self):
        return self.article.name

class Favourite(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='favs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favs')

    def __str__(self):
        return self.article.name