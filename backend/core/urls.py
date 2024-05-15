"""
URL patterns for our core app
"""

from core import views
from django.urls import path

urlpatterns = [
    path("hello/", views.HelloApp.as_view()),
]
