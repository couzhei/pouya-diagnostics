from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def hello_world_drf(request, *args, **kwargs):
    return Response(data={"msg": "Hello from rest api"})


# Create your views here.
def hello_app(request):
    return HttpResponse("Hello from demo_app1!")


# This is a demo of django's API versioning
@api_view(["GET"])
def demo_version(request, *args, **kwargs):
    version = request.version
    return Response(data={"msg": f"You have hit {version} of demo-api"})
