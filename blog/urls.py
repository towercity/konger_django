from . import views
from django.urls import path
from django.views.generic import RedirectView


urlpatterns = [
    path('',  RedirectView.as_view(url='blog/', permanent=True)),
    path('<slug:slug>', views.PageView.as_view(), name='page'),
    path('blog/', views.PostList.as_view(), name='post_list'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]