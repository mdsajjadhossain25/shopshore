# Generated by Django 4.2.4 on 2023-10-01 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_features_product_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shipping_option',
            field=models.TextField(blank=True, max_length=700),
        ),
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.TextField(blank=True, max_length=700),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.TextField(blank=True, max_length=700),
        ),
    ]
