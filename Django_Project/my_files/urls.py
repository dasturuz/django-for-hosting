from django.urls import path
from . views import *

urlpatterns = [
     path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
     path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name="post_editor"),
     path('post/new/',CreaterBlog.as_view(),name="new_post"),
     path('',HomePage.as_view(),name="home"),
     path('about/',About.as_view(),name="about"),
     path("post/<pk>/",BlogDetailView.as_view(),name='post_detail')
]