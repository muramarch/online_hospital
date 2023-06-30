from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps.accounts.models import User
from django.contrib.auth.decorators import login_required
from apps.appointments.models import Appointment
from apps.base.forms import AppointmentForm
from apps.base.models import Department
from django.db.models import Q

@login_required(login_url='/login')
def appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    context = {'appointment': appointment}
    return render(request, 'appointments/appointment.html', context)

@login_required(login_url='/login')
def createAppointment(request):
    form = AppointmentForm()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('view-appointment')

    context = {'form': form}
    return render(request, 'appointments/form_appointment.html', context)

@login_required(login_url='/login')
def viewAppointment(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    appointments = Appointment.objects.filter(
        Q(dept__name__icontains=q) |
        Q(title__icontains=q) |
        Q(patient__username__icontains=q)
    )

    departments = Department.objects.all()
    appointment_count = appointments.count()

    context = {
        'appointments': appointments,
        'departments': departments,
        'appointment_count': appointment_count,
    }
    return render(request, 'appointments/view_appointment.html', context)

@login_required(login_url='/login')
def updateAppointment(request, pk):
    try:
        appointment = Appointment.objects.get(id=pk)
    except Appointment.DoesNotExist:
        return HttpResponse("Appointment does not exist!")

    form = AppointmentForm(instance=appointment)

    if request.user != appointment.patient:
        return HttpResponse("Access Denied!")

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('view-appointment')

    context = {'form': form}
    return render(request, 'appointments/form_appointment.html', context)

@login_required(login_url='/login')
def deleteAppointment(request, pk):
    try:
        appointment = Appointment.objects.get(id=pk)
    except Appointment.DoesNotExist:
        return HttpResponse("Appointment does not exist!")

    if request.user != appointment.patient:
        return HttpResponse("Access Denied!")

    if request.method == 'POST':
        appointment.delete()
        return redirect('view-appointment')

    return render(request, 'appointments/delete.html', {'obj': appointment})
