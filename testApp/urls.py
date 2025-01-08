from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_item, name='create_item'),
    path('item/<int:item_id>/', views.get_item, name='get_item'),
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]