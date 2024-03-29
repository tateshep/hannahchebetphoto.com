"""photova URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('gallery/',include('gallery.urls')),
    path('userprofil/',include('django.contrib.auth.urls')),
    path('userprofile/',include('userprofile.urls')),
    # path('sendemail/',include('sendemail.urls')), Turning this off to hopefully hide the contact form and prevent spam
    path('blog/',include('blog.urls')),
    path('comments/',include('django_comments.urls')),
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
