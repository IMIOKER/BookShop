# Generated by Django 3.2.7 on 2021-09-16 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='book.Items'),
        ),
    ]