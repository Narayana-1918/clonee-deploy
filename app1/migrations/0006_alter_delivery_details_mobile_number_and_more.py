# Generated by Django 5.0.4 on 2024-06-14 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_delivery_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery_details',
            name='mobile_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='delivery_details',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
