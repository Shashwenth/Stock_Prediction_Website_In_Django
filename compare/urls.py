# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('compare/', views.stock_details, name='stock_details'),
    path('link-to-project1/', views.link_to_project1, name='link_to_project1'),
    # ... other URL patterns ...
]
