from django.db.models.signals import post_delete
from django.dispatch import receiver

from main.models import TaskDocument, Task
from utils.upload import task_delete_path, doc_delete_path


@receiver(post_delete, sender=Task)
def task_deleted(sender, instance, **kwargs):
    if instance.docs.count() > 0:
        for doc in instance.docs:
            task_delete_path(document=doc.document)

@receiver(post_delete, sender=TaskDocument)
def taskdoc_deleted(sender, instance, **kwargs):
    doc_delete_path(document=instance.document)