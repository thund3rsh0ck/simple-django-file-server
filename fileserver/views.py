from django.shortcuts import render
from django.http import HttpResponse

#What our fileserver will render.. for now let's just have some http
def index(request):
    return HttpResponse("Welcome to our simple fileserver")
