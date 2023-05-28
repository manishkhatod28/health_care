"""health_care URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

import healthCare
from healthCare.views import daily_health_routine, get_meditation_sessions
# from helthCare.views import get_meditation_sessions

from django.urls import path

urlpatterns = [
    # Other URL patterns in your project
    path('login/',healthCare.views.login),
    path('daily-health-routine/', healthCare.views.daily_health_routine, name='daily_health_routine'),
    path('meditation/sessions/', healthCare.views.get_meditation_sessions, name='get_meditation_sessions'),
]
