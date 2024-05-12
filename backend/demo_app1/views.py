from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# DRF gives us @api_view to work with regular Django
# functional views. Adding the decorator converts the
# usual Django HttpRequest into a Request instance.


# The decorator takes a list of all the HTTP-allowed methods for the
# given functional view block; any method that is not listed will
# not be allowed. By default, if no HTTP method is mentioned, then
# it will only allow GET methods.
@api_view(["GET", "POST", "PUT"])
def hello_world_drf(request, *args, **kwargs):
    # For a response to views, we should use
    # the Response class from DRF rather than
    # HttpResponse from Django; it automatically
    # takes care of bypassing cross-site request
    # forgery (CSRF) for views and gives us a UI
    # to interact with the backend service.
    if request.method == "POST":
        return Response(data={"msg": "POST response block from the rest api"})
    elif request.method == "PUT":
        return Response(data={"msg": "PUT response block from the rest api"})
    return Response(data={"msg": "Hello from the rest api via GET response block"})


# Create your views here.
def hello_app(request):
    return HttpResponse("Hello from demo_app1!")


# This is a demo of django's API versioning
# Here's a summary of the things involved:
# First, we added REST_FRAMEWORK = {
#     "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning"
# } to our settings.py.
# Then, we defined a URL path containing <version>, in our main urlpatterns
# which is the standard
# way of handling the version and DRF expects it to be that name by default
# We added a new url into our main urlpatterns which is included.
# Thereafter, we defined a new url into our demo_app1's urlpatterns
# (I still can't see why is this separation of urlpatterns)
# Finally, once we have configured the URL with the <version>,
# we can try to create a new view and retrieve the version in our view
@api_view(["GET"])
def demo_version(request, *args, **kwargs):
    version = request.version
    return Response(data={"msg": f"You have hit {version} of demo-api"})


# We see that it returns any version the user provide. This
# might so this might create confusion for the end user hitting
# the endpoint. To solve this problem, we shall see how we can
# customize the version class of DRF so that we can add constraints
# that can help us design better applications.
# First, create a file called demo_app/custom_versions.py.
# This file will have a custom version class for each view,
# along with a default class for all the views that don’t
# have multiple versions yet


# we integrate the custom version class (note that the custom versioning_class
# can be only linked to a class-based view, so we are using APIView here)

from demo_app1 import custom_versions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# DRF provides two types of class-based views: APIView and Generic Views.
from rest_framework.views import APIView

# Let’s implement a quick example with APIView to learn more:

# from rest_framework.views import APIView
# class DemoAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response(data={'msg': 'get request block'})
#     def post(self, request, *args, **kwargs):
#         return Response(data={'msg': 'post request block'})
#     def delete(self, request, *args, **kwargs):
#         return Response(data={'msg': 'delete request block'})
# Linking an APIView implemented class to the urls.py file is different
# from how we linked functional views earlier. Instead, we use <class name>.as_view()
# to link it to the corresponding URL:

# urlpatterns = [
#     ...
#     path('apiview-class/', views.DemoAPIView.as_view())
# ]


# first exposure to Class-based Views
# the custom versioning_class can be only
# linked to a class-based view, so we are using APIView here
# note that for the time being, the View and APIView are the same in this context
# and we'll get to the minor detailed differences later
class DemoView(APIView):
    # Using the APIView class converts the default Django HttpRequest into
    # a Request object, and the handler methods can return DRF’s
    # Response object rather than Django’s HttpResponse. It supports
    # additional policy attributes such as authentication_classes,
    # permission_classes, and versioning_classes, which make the
    # life of a developer much easier.
    versioning_class = custom_versions.DemoViewVersion

    def get(self, request, *args, **kwargs):
        version = request.version
        return Response(data={"msg": f" You have hit {version}"})


class AnotherView(APIView):
    versioning_class = custom_versions.AnotherViewVersion

    def get(self, request, *args, **kwargs):
        version = request.version

        # we can also define different logics for different versions
        if version == "v1":
            # perform v1 related tasks
            return Response(data={"msg": "v1 logic"})
        elif version == "v2":
            # perform v2 related tasks
            return Response(data={"msg": "v2 logic"})


# don't forget that these Views can only be accessible if
# their corresponding url pattern is provided
