from django.shortcuts import render, redirect, get_object_or_404
from .models import Maintenance
from .forms import MaintenanceForm

def maintenance_view(request):
    maintenances = Maintenance.objects.all()
    return render(request, 
                  'maintenance_templates/maintenance_list.html',
                  {'maintenances': maintenances}
                  )

def maintenance_create_view(request):
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

def maintenance_update_view(request, maintenance_id):
    maintenance = get_object_or_404(Maintenance, pk=maintenance_id)
    if request.method == 'POST':
        form = MaintenanceForm(request.POST, instance=maintenance)
        if form.is_valid():
            form.save()
            return redirect(maintenance_view)  
    else:
        form = MaintenanceForm(instance=maintenance)
    return render(request, 
                  'maintenance_templates/maintenance_form.html', 
                  {'form': form}
                  )

def maintenance_delete_view(request, maintenance_id):
    maintenance = get_object_or_404(Maintenance, pk=maintenance_id)
    if request.method == 'POST':
        maintenance.delete()
        return redirect(maintenance_view)  
    return render(request, 
                  'maintenance_templates/maintenance_confirm_delete.html', 
                  {'maintenance': maintenance}
                  )