# Generated by Django 3.1.3 on 2021-06-16 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210614_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='starting_bid',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.FloatField()),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auction_listing')),
            ],
        ),
    ]
