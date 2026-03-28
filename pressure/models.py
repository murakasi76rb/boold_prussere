from django.db import models

# Create your models here.
from django.contrib.auth.models import  AbstractUser

class Gender(models.TextChoices):
    MALE ='m', 'Male'
    FEMALE = 'f', 'Female'



class User(AbstractUser):
    gender = models.CharField(max_length=1, choices=Gender, default=Gender.MALE)
    age = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self) -> str:
        return  f'{self.first_name} {self.last_name} {self.age} {self.get_gender_display()}' # type: ignore