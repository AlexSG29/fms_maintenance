from django.db import models

# Create your models here.
class Contact(models.Model):
    CONTACT_TYPE_CHOICES = (
        ('proveedor', 'Proveedor'),
        ('trabajador', 'Trabajador'),
    )

    name = models.CharField(max_length=255)
    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPE_CHOICES)
    role = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name