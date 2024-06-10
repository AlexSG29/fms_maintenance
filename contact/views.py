from django.shortcuts import render
from .models import Contact


def contact_view(request):
    contacts = Contact.objects.all()
    return render(request, 
                  'contact_templates/contact_list.html',
                  {'contacts': contacts}
                  )

