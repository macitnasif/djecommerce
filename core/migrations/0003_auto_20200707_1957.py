# Generated by Django 2.2.8 on 2020-07-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200707_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='-'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('-', '----'), ('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear')], default='-', max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('-', '----'), ('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='-', max_length=1),
        ),
    ]
