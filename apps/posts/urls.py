from pyexpat import native_encoding

from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostListView.as_view(), name ='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail')
]
