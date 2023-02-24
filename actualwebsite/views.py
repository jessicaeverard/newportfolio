from django.shortcuts import render
from .forms import ContactForm

def index(request):
    if request.method == 'POST': #method is post as we are inputting data
        form = ContactForm(request.POST) #creating an instance for this form
        newContact = form.save(commit=False)
        newContact.save()
    return render(request, "home.html", {'form':ContactForm})
