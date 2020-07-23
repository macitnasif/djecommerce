# Generated by Django 2.2.8 on 2020-07-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('-', '---'), ('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear')], default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('-', '---'), ('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='-', max_length=1),
        ),
    ]
