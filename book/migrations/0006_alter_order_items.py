# Generated by Django 3.2.7 on 2021-09-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_items_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='book.Items'),
        ),
    ]
