"""
URL configuration for petProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from main_routing.views import (start_page,
                                home_page,
                                login_page,
                                registration_page)
from login.views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth', LoginAPIView.as_view(), name='api-auth'),
    path('api/v1/registration', RegistrationAPIView.as_view(), name='api-registration'),

    path('', start_page, name='start_page'),
    path('login/', login_page, name='login'),
    path('registration/', registration_page, name='registration'),
    path('home/', home_page, name='home'),
]
