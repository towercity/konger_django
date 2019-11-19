from . import views
from django.urls import path


urlpatterns = [
    path('<slug:slug>', views.PageView.as_view(), name='page'),
    path('blog/', views.PostList.as_view(), name='post_list'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]