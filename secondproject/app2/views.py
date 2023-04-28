from django.shortcuts import render
import datetime
import random
# Create your views here.
def astrology_view(request):
    time=datetime.datetime.now()
    dt=int(time.strftime('%H'))
    list=['Darshan','Priyanshu','Deepanshu']
    msg1 = 'Mr.'+ random.choice(list)
    msg2='Good'
    if dt<12:
        msg2 = msg2 + 'morning'
    elif dt<16:
        msg2 = msg2 + 'afternoon'
    elif dt<21:
        msg2 = msg2 + 'evening'
    else:
        msg2 = msg2 + 'night'

    astrology_list = ['Golden days ahead', 'Better to sleep more time in office',
                'Tomorrow will be best day of you life',
                'very soon you will be get hike or better job']
    astrology=random.choice(astrology_list)
    context={
        'time':time,
        'msg1':msg1,
        'msg2':msg2,
        'astrology': astrology
    }

    return render(request,'astrology.html',context)