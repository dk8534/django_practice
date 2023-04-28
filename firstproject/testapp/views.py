from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

# simple view function to display mesg to enduser.

def display(request):
    #print(type(Request)) # the o/p will display on terminal console after running the server and give path
    s='<h1>Hi!.. This is a home page.</h1>'
    print(len(s)) # iska o/p terminal screen par dikhega afer running the server and sending the request url.
    return HttpResponse(s)

# view function to get real server date and time.

def getdatetime(request):
    dt_1 = datetime.datetime.now()
    dt_2 = '<h1>' ,dt_1 ,'</h1>' # to formating with HTML tag
    return HttpResponse(dt_2)
    # return HttpResponse('<h1>Real Date and time is: </h1>',dt)    having the doubt in this line 


# Dynamic view function to sent the greeting message to enduser based on time.

def get_greeting_mesg(request):
    dt = datetime.datetime.now()
    hour = int(dt.strftime('%H'))
    mesg = '<h1> Hello Friend!'
    if hour < 12:
        mesg = mesg + 'Good Morning'
    elif hour < 16:
        mesg = mesg + 'Good Afternoon'
    elif hour < 21:
        mesg = mesg + 'Good Evening'
    else:
        mesg = mesg + 'Good Night'
    
    mesg = mesg + '<hr>' + 'The Real Sever Date and Time is ' + str(dt) + '</h1> ' 


    return HttpResponse(mesg)

# this is also a way to define html code inside python file but not recomended because reusability of app not working , code mix with python and html.

# def home_view(request):
    
    # s='''<h1>Hello! This is home page</h1>
    # <h2>My Hobbies:</h2>
    # <ul>
    #     <li>online gamming</li>
    #     <li>video editing</li>
    #     <li>web surfing</li>
    #     <li>coding</li>
    # </ul>'''

    # return HttpResponse(s)

# this is recomended way.

def home_view(request):
    return render(request,'testapp/home.html')