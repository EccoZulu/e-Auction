# Generated by Django 4.1.7 on 2023-04-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_current_highest_bid_product_currenthighestbid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='currentHighestBid',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
