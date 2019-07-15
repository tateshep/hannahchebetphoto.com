from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('',views.homeView, name='index'),
    path('view-admin',views.adminView, name ='admin_view'),
]