from home.models import Doctor, Patient, appointment
from django.contrib import admin

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(appointment)