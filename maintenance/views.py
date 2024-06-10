from django.shortcuts import render, redirect
from .models import Maintenance
from .forms import MaintenanceForm

def maintenance_view(request):
    maintenances = Maintenance.objects.all()
    return render(request, 
                  'maintenance_templates/maintenance_list.html',
                  {'maintenances': maintenances}
                  )

def contact_create_view(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(maintenance_view) 
    else:
        form = MaintenanceForm()
    return render(request, 
                  'maintenance_templates/maintenance_form.html', 
                  {'form': form}
                  )