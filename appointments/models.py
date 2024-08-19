from django.db import models
from random import randint, randrange
from django.db.models.fields import IntegerField
from django.utils.crypto import get_random_string

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=64)  
    id = models.BigAutoField(primary_key=True)
    notes = models.CharField(max_length=1000, default="")

    def __str__(self):
        return f"{self.name} "

    def save(self,*args, **kwargs):
        if not self.id:
            is_unique = False
            while not is_unique:
                checkId = randint(99999, 999999) # 19 digits: 1, random 18 digits
                is_unique = not Patient.objects.filter(id=checkId).exists()
            self.id = checkId
        super(Patient, self).save(*args, **kwargs)

class Appointment(models.Model):

    date = models.DateField() 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    department = models.CharField(max_length=64)
    
    def __str__(self):
        return f"Appointment {self.id}: {self.patient} with {self.department} department on {self.date}"