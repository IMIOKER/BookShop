# Generated by Django 3.2.7 on 2021-09-16 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='book.Items'),
        ),
    ]
