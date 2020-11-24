from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['lakshayjindal01@gmail.com'])
            return HttpResponse('Thanks for contacting us!')
        else:
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})
