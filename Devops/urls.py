"""Devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls import include
from main import views as main_views
import menu.urls
from main import urls as main_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/', main_views.login, name='login'),
    url(r'^logout/', main_views.logout, name='logout'),
    url(r'^main/', main_views.mainpage),
    url(r'^user/', include(main_urls)),
    url(r'^menumanager/', include(menu.urls)),
    url(r'^Account', include('Account.urls')),
    url(r'^jenkins/', include('jenkins.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
