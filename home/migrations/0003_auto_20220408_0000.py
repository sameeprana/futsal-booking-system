# Generated by Django 3.2.12 on 2022-04-07 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_login_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='last_name',
            new_name='lastname',
        ),
    ]