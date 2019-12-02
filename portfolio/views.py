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
    template_name = 'portfolio/projects.html'

class Projects(Index):
    def get_queryset(self):
        return Project.objects.filter(display=1).filter(languages__name__iexact=self.kwargs['lang_name'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language_list'] = Language.objects.filter(show_in_bar=1)
        context['page_title'] = Language.objects.filter(name__iexact=self.kwargs['lang_name'])
        return context

    template_name = 'portfolio/langs.html'