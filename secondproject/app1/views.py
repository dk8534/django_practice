from django.shortcuts import render
import datetime
# Create your views here.

def template_view(request):
    time=datetime.datetime.now()
    # context={'time':time}   #template tags : to insert daynamic content into html file use template tags.
    return render(request,'index.html',{'time':time}) # 1st way (without context variable)
    # return render(request,'index.html,context={'time':time})  # 2nd way (with context variable)
    