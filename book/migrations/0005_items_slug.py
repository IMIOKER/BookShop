# Generated by Django 3.2.7 on 2021-09-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
