from django.contrib import admin

from .models import Appointment, Patient

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Patient)

