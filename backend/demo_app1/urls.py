from demo_app1 import views
from django.urls import path

urlpatterns = [
    path("hello-world/", views.hello_app),
    path("hello-world-drf/", views.hello_world_drf),
]
