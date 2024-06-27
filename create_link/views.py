from django.shortcuts import render
from random import choice
from .models import ShortLink
from datetime import datetime

# Create your views here.
def index(request):
    return render(request=request,template_name='index.html',context={"short_link":"None"})


def create_link(request):
    long_link = request.GET.get("longlink")
    short_link = request.GET.get("shortlink")
    print(short_link)
    if short_link is None or short_link == "":
        lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        short_link = ""
        for i in range(4):
            short_link += choice(lower)
        link = ShortLink.objects.get_or_create(long_link = long_link,short_link = short_link)
    else:
        if len(short_link)>4:
            lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            short_link = ""
            for i in range(4):
                short_link += choice(lower)
        link = ShortLink.objects.get_or_create(long_link = long_link,short_link = short_link)
    print(link)
    return render(request=request,template_name='index.html',context= {"short_link":link[0].short_link})
