# Generated by Django 5.0.4 on 2024-06-14 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_cart_items_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart_items',
            old_name='product',
            new_name='menu',
        ),
    ]
