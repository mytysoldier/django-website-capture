from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('capture', views.websiteCapture, name='webcapture'),
]