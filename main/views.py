from django.shortcuts import render
from django.utils.translation import gettext as _
# Create your views here.
from django.utils import translation


def homepage(request):
    return render(request = request, template_name='home.html')

def about(request):
    return render(request = request, template_name='about.html')

def services(request):
    return render(request = request, template_name='services.html')

def servicesoftware(request):
    return render(request = request, template_name='services software.html')

def servicedata(request):
    return render(request = request, template_name='services data services.html')

def contact(request):
    return render(request = request, template_name='contact.html')

