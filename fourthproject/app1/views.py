from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request,'home.html')


def news_view(request):
    news1='Mass-grave site runs out of space as endless stream of bodies overwhelms Marash'
    news2='ChatGPT powered Microsoft Bing refused to write a cover letter for a job, said it is unfair'
    news3='Here\'s why HAL\'s concept aircraft HLFT-42 has Lord Hanuman on its fin'
    news4='LTTE\'s Prabakaran is alive, will appear in public soon, claims Tamil leader'
    ok={'news1':news1,'news2':news2,'news3':news3,'news4':news4}
    return render(request,'news.html',ok)