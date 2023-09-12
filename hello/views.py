from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"hello/index.html")
def john(request):
    return HttpResponse("Hello John")
def cena(request):
    return HttpResponse("Hello Cena")
def random(request,name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })