# Generated by Django 4.2 on 2023-04-14 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_productcategory_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='base.productcategory'),
        ),
    ]
