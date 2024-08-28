from django.contrib import admin

from .models import Appointment, Department, Patient

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Department)

