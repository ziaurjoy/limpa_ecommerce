# Generated by Django 3.1.2 on 2020-10-18 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201018_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='photo',
            new_name='image',
        ),
    ]
