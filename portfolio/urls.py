from . import views
from django.urls import path
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.Index.as_view(), name='lang_list'),
    path('home', views.Index.as_view(), name='lang_list'),
]