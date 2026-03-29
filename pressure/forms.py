from django import forms
from pressure.models import BloodPressureRecord

class FormBloodPressureRecord(forms.ModelForm):
    class Meat:
        model =BloodPressureRecord
        fielda = ['systolic', 'diastolic', 'pulse', 'patient']
        lebales ={
            'systolic': 'SYS',
            'diastolic': 'DIA',
            'pulse': 'HR',
        }