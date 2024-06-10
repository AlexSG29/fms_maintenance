from django.contrib import admin

# Register your models here.
from .models import Maintenance

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('vehicle_plate', 'maintenance_type', 'work_order', 'creation_date', 'completed')
    list_filter = ('maintenance_type', 'completed')
    search_fields = ('vehicle_plate', 'work_order')
    date_hierarchy = 'creation_date'