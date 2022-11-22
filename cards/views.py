from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

import random

from .forms import CardCheckForm
from .models import Card

class CardListView(ListView):
    model = Card 
    queryset = Card.objects.all().order_by("box", "-date_created")

class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-create")

class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")

class BoxView(CardListView): # list only cards in that box instead of all
    template_name = "cards/box.html" # Need override as CardListView serves card_list.html by default
    form_class = CardCheckForm

    def get_queryset(self): # Return only cards in that box
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) # Get box number from GET Request
        context["box_num"] = self.kwargs["box_num"]
        if self.object_list: # Check if there are any cards in that box
            context["check_card"] = random.choice(self.object_list) # picks a random card
        return context

    def post(self, request, *args, **kwargs): # Define post method
            form = self.form_class(request.POST)
            if form.is_valid(): # checks if form valid on backend as 2nd layer
                card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
                card.move(form.cleaned_data["solved"])

            return redirect(request.META.get("HTTP_REFERER"))