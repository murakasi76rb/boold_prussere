from django.contrib import admin

# Register your models here.
from pressure.models import User, BloodPressureRecord

admin.site.register(User)
admin.site.register(BloodPressureRecord)