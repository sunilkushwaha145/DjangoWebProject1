from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html_content = "<a href='home'>Home</a>"
    return HttpResponse(html_content)
def Home(request):
    return HttpResponse('heloo on home')
