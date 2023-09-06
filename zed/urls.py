from django.urls import path
from . import views


urlpatterns =  [
    path('',views.index, name='index'),
    path('blog',views.blog, name='blog'),
    path('blog-details/<str:pk>',views.blogdetails, name='blog-details')
]

