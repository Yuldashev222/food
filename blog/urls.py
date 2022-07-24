from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:slug>/', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name='post_single'),
    path('', home, name='home'),
]
