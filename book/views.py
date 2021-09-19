from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def Home(request):
    Order.objects.get_or_create(user=request.user)
    item = Product.objects.all()
    order = Order.objects.get(user=request.user)
    context = {'items':item, 'order':order}
    return render(request, 'book/home.html', context)

def Detail(request, id):
    item = Product.objects.get(id=id)
    order = Order.objects.get(user=request.user)
    context = {'item':item, 'order':order}
    return render(request, 'book/detail.html', context)

def Cart(request):
    items = Items.objects.filter(user=request.user)
    orders = Order.objects.get(user=request.user)
    context = {'items':items, 'order':orders}
    return render(request, 'book/cart.html', context)

# for add an item to cart
def AddToCart(request, id):
    item = Product.objects.get(id=id)
    orderitem = Items.objects.create(user=request.user, item=item, slug=id)
    order = Order.objects.get_or_create(user=request.user)
    order[0].items.add(orderitem)
    return redirect('home')

# for adding more from an item
def add_more(request, slug):
    item = Product.objects.get(id=slug)
    orderitem = Items.objects.create(item=item, user=request.user, slug=item.id)
    order = Order.objects.get_or_create(user=request.user)
    order[0].items.add(orderitem)
    return redirect('cart')

# for remove an item from cart
def remove(request, slug):
    Items.objects.filter(slug=slug, user=request.user)[0].delete()
    return redirect('cart')

# for get more information of order
def Chackout(request):
    orders = Order.objects.get(user=request.user)
    if request.method == "POST":
        data = request.POST
        phone = data['phone']
        name = data['name']
        address = data['address']
        orders.phone = phone
        orders.name = name
        orders.address = address
        orders.des = str(Items.objects.filter(user=request.user))
        orders.save()
        return redirect('done')
    context = {'order':orders}
    return render(request, 'book/check.html', context)

# after pay =>
def Done(request):
    order = Order.objects.get(user=request.user)
    order.final = True
    order.save()
    Items.objects.filter(user=request.user).delete()
    return render(request, 'book/pay.html')