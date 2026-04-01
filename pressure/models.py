from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from django.contrib.auth.models import  AbstractUser

class Gender(models.TextChoices):
    MALE ='m', 'Male'
    FEMALE = 'f', 'Female'



class User(AbstractUser):
    gender = models.CharField(max_length=1, choices=Gender, default=Gender.MALE)
    date_of_birth = models.DateField(verbose_name='Date of birth', null=True, blank=True)

    def __str__(self) -> str:
        full_name = f'{self.first_name} {self.last_name}'.strip()
        return  full_name or self.username 

    @property
    def age(self)->int:
        if not self.date_of_birth:
            return 0
        today = timezone.now().date()
        return today.year - self.date_of_birth.year -((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        
    


class BloodPressureRecord(models.Model):
    systolic = models.PositiveIntegerField(validators=[MinValueValidator(50), MaxValueValidator(250)])
    diastolic = models.PositiveIntegerField(validators=[MinValueValidator(30), MaxValueValidator(150)])
    pulse = models.PositiveIntegerField(validators=[MinValueValidator(30), MaxValueValidator(220)])
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blood_pressure_records')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f'{self.patient} SYS/DIA: {self.systolic}/{self.diastolic} | HR {self.pulse} time: {self.created_at:%Y-%m-%d %H:%M}'
    
    class Meta:
        ordering =['-created_at']
