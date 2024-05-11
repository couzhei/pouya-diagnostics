from demo_app1 import views
from django.urls import path

urlpatterns = [
    path("hello-world/", views.hello_app),
]
