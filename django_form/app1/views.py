from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def django_forms(request):
    form = EmployeeForm()
    context = {'form': form}
    return render(request,'index.html',context)