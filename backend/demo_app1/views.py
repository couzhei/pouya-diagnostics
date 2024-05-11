from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_app(request):
    return HttpResponse("Hello from demo_app!")
