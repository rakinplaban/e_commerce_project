# Generated by Django 3.1.3 on 2021-06-27 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='comments',
        ),
    ]
