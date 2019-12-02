from . import views
from django.urls import path
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('blog/', views.PostList.as_view(), name='post_list'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('publications/', views.PublicationsList.as_view(), name="publications"),
    path('<slug:slug>/', views.PageView.as_view(), name='page'),
]