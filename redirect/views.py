from django.shortcuts import render,redirect,HttpResponse
from create_link.models import ShortLink
# Create your views here.

def redirect_(request,shortlink):
    try:
        link = ShortLink.objects.get(short_link = shortlink)
        return redirect(link.long_link)
    except:
        return redirect("http://127.0.0.1:8000")