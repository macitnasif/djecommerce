from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Order, OrderItem
from django.views.generic import ListView, DetailView
from django.utils import timezone


# def home(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, "home.html", context)


# def products(request):
#     return render(request, "product.html")


class HomeView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


def checkout(request):
    return render(request, "checkout.html")


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "The item quantity is updated.")
        else:
            order.items.add(order_item)
            messages.info(request, "This item is added to your cart.")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item is added to your cart.")
    return redirect('core:product', slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item is removed from your cart.")
        else:
            messages.info(request, "This item is not in your cart.")
    else:
        messages.info(request, "You do not have an active order.")
    return redirect('core:product', slug=slug)
