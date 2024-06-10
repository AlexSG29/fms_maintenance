from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.maintenance_view, name='maintenance_list'),
    path('create/', views.maintenance_create_view, name='maintenance_create'),
    path('maintenance/<int:maintenance_id>/edit/', views.maintenance_update_view, name='maintenance_edit'),
    path('maintenance/<int:maintenance_id>/delete/', views.maintenance_delete_view, name='maintenance_delete'),
]
