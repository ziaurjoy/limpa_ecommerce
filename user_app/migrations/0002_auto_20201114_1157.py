# Generated by Django 3.1.2 on 2020-11-14 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
