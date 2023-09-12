from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    now=datetime.datetime.now()
    return render(request,"holiday/index.html",{
      "holiday": now.weekday()==6 or now.weekday()==7
    })

