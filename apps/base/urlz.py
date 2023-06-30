from django.urls import path
from . import views

urlpatterns = [
    # HOME PAGE
    path('', views.home, name="home"),

    # OTHER PAGES
    path('about/', views.aboutPage, name="about"),
    path('gallery/', views.galleryPage, name="gallery"),
    path('services/', views.servicesPage, name="services"),
    path('contact/', views.contactPage, name="contact"),

    # CRUD - APPOINTMENT
]
