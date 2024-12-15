"""
URL configuration for responsive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', website, name='website'),
    path('anime_list/', anime_list, name='anime_list'),
    path('anime_list_2/', anime_list_2, name='anime_list_2'),
    path('anime_list_3/', anime_list_3, name='anime_list_3'),
    path('ongoing/', ongoing, name='ongoing'),
    path('ongoing_2/', ongoing_2, name='ongoing_2'),
    path('upcoming/', upcoming, name='upcoming'),
    path('upcoming_2/', upcoming_2, name='upcoming_2'),
    path('completed/', completed, name='completed'),
    path('web_2/', web_2, name='web_2'),
    path('web_3/', web_3, name='web_3'),
    path('login/', login, name='login'),
    path('password/', password, name='password'),
]