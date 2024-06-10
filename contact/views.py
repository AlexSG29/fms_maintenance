from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

def contact_view(request):
    contacts = Contact.objects.all()
    return render(request, 
                  'contact_templates/contact_list.html',
                  {'contacts': contacts}
                  )

def contact_create_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(contact_view) 
    else:
        form = ContactForm()
    return render(request, 
                  'contact_templates/contact_create.html', 
                  {'form': form}
                  )

def contact_update_view(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(contact_view)  
    else:
        form = ContactForm(instance=contact)
    return render(request, 
                  'contact_templates/contact_create.html', 
                  {'form': form}
                  )
""" 
def contact_delete_view(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_templates/contact_form.html')  
    return render(request, 
                  'contact_templates/contact_confirm_delete.html', 
                  {'contact': contact}
                  ) """
