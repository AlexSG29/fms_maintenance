from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.maintenance_view, name='maintenance_list'),
]