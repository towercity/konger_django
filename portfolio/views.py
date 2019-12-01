from django.shortcuts import render
from django.views import generic
from .models import Language

# Create your views here.
class Index(generic.ListView):
    queryset = Language.objects.filter(show_in_bar=1)
    template_name = 'home.html'