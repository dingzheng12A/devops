#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : urls.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-10-30
# @Desc  :
from django.urls import include,path
from django.conf.urls import url
from jenkins.views import jenkins_analyze,jenkins_chart
urlpatterns = [
    url(r'^analyze',jenkins_analyze,name="analyze"),
    url(r'^jenkins_chart',jenkins_chart,name="jenkins_chart")
]