from django.shortcuts import render

# Create your views here.

def AI_view(request):
    chat_bots={'b1':'Google Bard','b2':'Microsoft Bing','b3':'Chatsonic','b3':'Jasper Chat','b4':'Character AI','b5':'YouChat','b6':'OpenAI Playground','b7':'DialoGPT','b8':'Perplexity AI','b9':'Replika','b10':'chat GPT'}

    return render(request,'AI.html',chat_bots)