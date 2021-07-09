# Generated by Django 3.1.3 on 2021-07-07 16:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auto_20210706_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bids',
            name='bid',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]
