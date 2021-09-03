"""Algosoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static
from main import views

from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    path("", views.homepage),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('services/', views.services),
    path('servicesoftware/', views.servicesoftware),
    path('servicedata/', views.servicedata),
    path('contact/', views.contact),
    #path('i18n/', include('django.conf.urls.i18n')),
    #path('i18n/', include('django.conf.urls.i18n')),
 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
