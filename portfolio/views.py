from django.shortcuts import render
from django.views import generic
from .models import Language, Project


# Create your views here.
class Index(generic.ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language_list'] = Language.objects.filter(show_in_bar=1)
        return context

    queryset = Project.objects.filter(display=1)
    context_object_name = 'project_list'
    template_name = 'home.html'