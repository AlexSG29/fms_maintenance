from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.contact_view, name='contact_list'),
    path('create/', views.contact_create_view, name='contact_create'),
    path('contact/<int:contact_id>/edit/', views.contact_update_view, name='contact_edit'),
]