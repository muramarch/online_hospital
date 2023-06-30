from django.shortcuts import render, redirect

from apps.accounts.models import Doctor


# hospital
def home(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'base/home.html', context)


# hospital
def aboutPage(request):
    context = {}
    return render(request, 'base/about.html', context)

# hospital
def galleryPage(request):
    context = {}
    return render(request, 'base/gallery.html', context)

# hospital
def servicesPage(request):
    context = {}
    return render(request, 'base/services.html', context)

# hospital
def contactPage(request):
    context = {}
    return render(request, 'base/contact.html', context)

