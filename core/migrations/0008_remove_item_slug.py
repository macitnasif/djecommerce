# Generated by Django 2.2.8 on 2020-07-09 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_item_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='slug',
        ),
    ]
