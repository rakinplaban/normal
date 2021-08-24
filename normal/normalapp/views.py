from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import json
# Create your views here.


def index(request):
    with open("stock_market_data.json", "r") as readit:
        jsonobject = json.load(readit)
    
        return render(request,"normalapp/index.html",{
            "jsonobject" : jsonobject
        })