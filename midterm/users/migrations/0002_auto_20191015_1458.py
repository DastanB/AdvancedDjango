# Generated by Django 2.1.2 on 2019-10-15 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
