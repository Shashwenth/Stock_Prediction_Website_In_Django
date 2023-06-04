from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('link-to-project2/', views.link_to_project2, name='link_to_project2'),
    path('link-to-project3/', views.link_to_project3, name='link_to_project3'),
    path('link-to-project1/', views.link_to_project1, name='link_to_project1'),
]