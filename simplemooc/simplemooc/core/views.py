from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

CONTACT_TEMPLATE = 'contact.html'
HOME_TEMPLATE = 'home.html'


def home(request):
    return render(request, HOME_TEMPLATE)


def contact(request):
    return render(request, CONTACT_TEMPLATE)
