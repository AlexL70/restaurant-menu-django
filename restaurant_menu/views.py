from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("meal_type", "meal")
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["meal_types"] = MEAL_TYPE
        context["items"] = self.queryset
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
