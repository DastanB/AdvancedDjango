import os
import shutil
from datetime import datetime

def article_image_path(instance, filename):
    article = instance.article
    article_id = article.id
    return f'articles/{article_id}/images/{filename}'

def article_image_delete_path(document):
    path = os.path.abspath(os.path.join(document.path, '..'))
    print(path)
    shutil.rmtree(path)

def article_delete_path(document):
    path = os.path.abspath(os.path.join(document.path, '../..'))
    print(path)
    shutil.rmtree(path)