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
    description = models.TextField()
    number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name