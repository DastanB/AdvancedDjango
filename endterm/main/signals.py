from django.db.models.signals import post_delete
from django.dispatch import receiver

from main.models import Article, ArticleImage
from utils.upload import article_delete_path, article_image_delete_path


@receiver(post_delete, sender=Article)
def article_deleted(sender, instance, **kwargs):
    if instance.images.count() > 0:
        for img in instance.images:
            article_delete_path(document=img.image)

@receiver(post_delete, sender=ArticleImage)
def article_image_deleted(sender, instance, **kwargs):
    article_image_delete_path(document=instance.image)