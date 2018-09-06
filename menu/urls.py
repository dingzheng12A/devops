#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : urls.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-8-29
# @Desc  :
from django.urls import path
from django.conf.urls import include,url
from menu.views import addmenu,addsubmenu,delmenu,editmenu

urlpatterns = [
    url(r'^addmenu/',addmenu),
    url(r'^addsubmenu/',addsubmenu),
    url(r'^delmenu/',delmenu),
    url(r'^editmenu/',editmenu),
]
