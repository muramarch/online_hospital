from django.urls import path
from . import views

urlpatterns = [
    path('appointment/<str:pk>/', views.appointment, name="appointment"),
    path('create-appointment/', views.createAppointment, name="create-appointment"),
    path('view-appointment/', views.viewAppointment, name="view-appointment"),
    path('update-appointment/<str:pk>/', views.updateAppointment, name="update-appointment"),
    path('delete-appointment/<str:pk>/', views.deleteAppointment, name="delete-appointment"),

]