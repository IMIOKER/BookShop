from typing import final
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    price = models.CharField(max_length=100)
    exist = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

class Items(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)# for gat a unic id

    def get_tot(self):
        return self.item.price

    def __str__(self):
        return str(self.item)


class Order(models.Model):
    items = models.ManyToManyField(Items)#for calculate final price
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    final = models.BooleanField(default=False)# for check the order status
    phone = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    address = models.TextField()
    des = models.TextField(null=True, blank=True)# for get items of order (Items)

    def get_final(self):# for return the final price
        total = 0
        for item in self.items.all():
            total += int(item.get_tot())
        return total

    def cart_items(self):
        items = 0
        for item in self.items.all():
            items += 1
        return items

    def __str__(self) -> str:
        return str(self.final)
