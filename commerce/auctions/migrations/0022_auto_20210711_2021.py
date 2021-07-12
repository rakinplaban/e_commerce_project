# Generated by Django 3.1.3 on 2021-07-11 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_auction_listing_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='auction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction', to='auctions.auction_listing'),
        ),
    ]
