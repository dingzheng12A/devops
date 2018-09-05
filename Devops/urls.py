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
from Role import views as role_views
import menu.urls
#from django.conf import settings
#from django.views.static import serve
import os,sys

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/', main_views.login,name='login'),
    url(r'^logout/', main_views.logout),
    url(r'^main/', main_views.mainpage),
    url(r'^addUser/', main_views.adduser,name='adduser'),
    url(r'^dropUser', main_views.dropuser,name='dropuser'),
    url(r'^addRole',main_views.add_role),
    url(r'^dropRole', main_views.dropRole),
    url(r'^userinfo/', main_views.userinfo),
    url(r'^adduser', main_views.add_user),
    url(r'^resetpass', main_views.resetpass),

    url(r'^deluser', main_views.deluser),
    url(r'^addrole', main_views.addrole),

    url(r'^rolelist', main_views.roleinfo),
    url(r'^assign',main_views.assign),
    url(r'^removeassign', main_views.removeassign),
    url(r'^menumanager/',include(menu.urls)),
    url(r'^download/',main_views.download,name='download')


]
