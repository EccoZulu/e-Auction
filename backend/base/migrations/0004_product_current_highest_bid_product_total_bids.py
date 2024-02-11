# Generated by Django 4.1.7 on 2023-04-01 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='current_highest_bid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='total_bids',
            field=models.IntegerField(default=0),
        ),
    ]
