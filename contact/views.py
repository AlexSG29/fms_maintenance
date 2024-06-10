from django.shortcuts import render
from .models import Contact


def contact_view(request):
    return render(request, 'contact_app_templates/contact_list.html')

""" def contacts_detail_view(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    return render(request, 
                  'contacts_app_templates/contacts.html', 
                  {'contact': contact}
                  ) """
