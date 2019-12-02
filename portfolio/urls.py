from . import views
from django.urls import path
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('home', views.Index.as_view(), name='home'),
    path('lang/<lang_name>', views.Projects.as_view(), name='lang_view'),
]