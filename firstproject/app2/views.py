from django.shortcuts import render
from django.http import HttpResponse as HR

# Create your views here.

def app2_view(request):
    s='<h1> Hello! This is app2 view page </h1>'
    return HR(s)


def index_view(request):
    return render(request,'app2/index.html')