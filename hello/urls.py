from . import views
from django.urls import path

urlpatterns=[
      path("",views.index,name="new"),
      path("john",views.john,name="john"),
      path("<str:name>",views.random,name="random"),
      path("cena",views.cena,name="cena")
      
]