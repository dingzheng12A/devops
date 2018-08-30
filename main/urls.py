#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : urls.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-8-8
# @Desc  :
from django.urls import path
from django.conf.urls import url
from main import views
urlpatterns = [
    url(r'^aaa/', views.login,name='login'),
    url(r'^logout/', views.logout),
    url(r'^$', views.listuser),
    url(r'^userinfo/', views.userinfo),
    url(r'^adduser', views.adduser),
    url(r'^resetpass', views.resetpass),
    url(r'^deleteuser', views.dropuser),
    url(r'^deluser', views.deluser),
    url(r'^addrole', views.addrole),
    url(r'roleinfo', views.listuser),
    url(r'^delrole', views.delrole),
    url(r'^rolelist', views.roleinfo),
    url(r'^assign', views.assign),
    url(r'^removeassign', views.removeassign),


]