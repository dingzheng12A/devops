#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : urls.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-10-25
# @Desc  :
from django.urls import path
from django.conf.urls import url
from Account.views import  Billing
urlpatterns = [
    url(r'Billing',Billing)
]