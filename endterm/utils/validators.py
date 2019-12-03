import os
from django.core.exceptions import ValidationError
from utils.constants import TASK_ALLOWED_EXTS


def article_image_size(value):

    if value.size > 200000:
        raise ValidationError('invalid file size')


def article_image_extension(value):
    ext = os.path.splitext(value.name)[1]

    if not ext.lower() in TASK_ALLOWED_EXTS:
        raise ValidationError(f'not allowed ext, allowed ({TASK_ALLOWED_EXTS})')