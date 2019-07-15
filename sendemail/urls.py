from django.contrib import admin
from django.urls import path

from .views import contactView, successView

app_name = "sendemail"

urlpatterns = [
    path('contact/', contactView, name='contact'),
    path('contact/success/', successView, name='success'),
]
