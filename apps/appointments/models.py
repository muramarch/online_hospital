from django.db import models
from apps.accounts.models import User

from apps.base.models import Department

class Appointment(models.Model):
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField()
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # Hii ni kwaajili ya ku-order (ascending or descending) appointments
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name