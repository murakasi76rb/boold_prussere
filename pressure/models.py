from django.db import models

# Create your models here.
from django.contrib.auth.models import  AbstractUser

class Gender(models.TextChoices):
    MALE ='m', 'Male'
    FEMALE = 'f', 'Female'



class User(AbstractUser):
    gender = models.CharField(max_length=1, choices=Gender, default=Gender.MALE)
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        full_name = f'{self.first_name} {self.last_name}'.strip()
        return  full_name or self.username
    


class BloodPressureRecord(models.Model):
    systolic = models.PositiveIntegerField()
    diastolic = models.PositiveIntegerField()
    pulse = models.PositiveIntegerField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blood_pressure_records')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.patient} SYS/DIA: {self.systolic}/{self.diastolic} | HR {self.pulse} time: {self.created_at:%Y-%m-%d %H:%M}'
