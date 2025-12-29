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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views
from main.views_i18n import set_language_custom
from django.utils.translation import gettext_lazy as _

# Non-translated URLs
urlpatterns = [
    path('i18n/setlang/', set_language_custom, name='set_language'),  # Custom i18n view
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Translated URLs
urlpatterns += i18n_patterns(
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('servicesoftware/', views.servicesoftware, name='servicesoftware'),
    path('servicedata/', views.servicedata, name='servicedata'),
    path('contact/', views.contact, name='contact'),
    prefix_default_language=True
)
