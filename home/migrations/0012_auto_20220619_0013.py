# Generated by Django 3.2.12 on 2022-06-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_getdatetime_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='getdatetime',
            name='time',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='getdatetime',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
