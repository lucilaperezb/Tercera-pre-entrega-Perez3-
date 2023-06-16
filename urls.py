from django.urls import path
from . import views

urlpatterns = [
    path('insert-data/', views.insert_data, name='insert_data'),
    path('search-data/', views.search_data, name='search_data'),
]
