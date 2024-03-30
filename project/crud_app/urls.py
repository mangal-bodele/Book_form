from django.urls import path
from .views import add_book,show_book,update_book,delete_book

urlpatterns  = [
    path('add/',add_book, name='add_url'),
    path('show/',show_book, name='show_url'),
    path('update/<int:pk>/',update_book, name='update_url'),
    path('delete/<int:pk>/',delete_book, name='delete_url')
]