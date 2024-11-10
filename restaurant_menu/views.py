from django.shortcuts import render
from django.views import generic
from .models import Item


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("meal_type", "meal")
    template_name = "index.html"


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
