from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.contact_view, name='contact_view'),
]