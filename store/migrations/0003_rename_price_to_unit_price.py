# Generated by Django 3.2.8 on 2021-10-14 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_add_slug_to_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]
