from django.db import models
from contact.models import Contact

class Maintenance(models.Model):
    VEHICLE_MAINTENANCE_CHOICES = [
        ('Correctivo', 'Correctivo'),
        ('Predictivo', 'Predictivo'),
    ]
    vehicle_plate = models.CharField(max_length=8)
    maintenance_type = models.CharField(
        max_length=20, 
        choices=VEHICLE_MAINTENANCE_CHOICES
        )
    workers = models.ManyToManyField(Contact)
    work_order = models.CharField(max_length=100, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)
    parts_replaced = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vehicle_plate} - {self.maintenance_type} - {self.work_order}"