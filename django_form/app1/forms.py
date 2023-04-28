from django import forms
from django.forms.widgets import DateInput

class EmployeeForm(forms.Form):
    ename = forms.CharField(max_length=500)
    eid = forms.IntegerField()
    joining_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    esalary = forms.IntegerField()