from django import forms
from pressure.models import BloodPressureRecord

class FormBloodPressureRecord(forms.ModelForm):
    class Meta:
        model =BloodPressureRecord
        fields = ['systolic', 'diastolic', 'pulse', 'patient']
        lebals ={
            'systolic': 'SYS',
            'diastolic': 'DIA',
            'pulse': 'HR',
        }
        



form = FormBloodPressureRecord()