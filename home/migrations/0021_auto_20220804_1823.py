# Generated by Django 3.2.12 on 2022-08-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20220804_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='unique_booking_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='product_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
