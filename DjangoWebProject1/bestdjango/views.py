from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    now =datetime.date.today()
    return render(
        request,
        "bestdjango/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )
def Home(request):
    return HttpResponse('heloo on home')
def MyItems(request):
    now =datetime.date.today()
    return render(
        request,
        "bestdjango/MyItems.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'message' : "Hello Django!",
            'content' : " on ",
        }
    )