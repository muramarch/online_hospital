from django.forms import ModelForm
from apps.appointments.models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

        # nataka user = patient, so achukuliwe automatic
        exclude = ['patient']