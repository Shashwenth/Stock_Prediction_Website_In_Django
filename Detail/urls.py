# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('detail/', views.stock_details, name='stock_details'),
    path('link-to-project2/', views.link_to_project2, name='link_to_project2'),
    # ... other URL patterns ...
]
