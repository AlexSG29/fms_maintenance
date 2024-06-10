from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_type', 'number', 'email', 'active')
    list_filter = ('contact_type', 'active')
    search_fields = ('name', 'number', 'email', 'role')
