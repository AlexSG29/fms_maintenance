from django.shortcuts import render
from .models import Maintenance

def maintenance_view(request):
    maintenances = Maintenance.objects.all()
    return render(request, 
                  'maintenance_templates/maintenance_list.html',
                  {'maintenances': maintenances}
                  )