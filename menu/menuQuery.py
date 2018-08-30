#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : menuQuery.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-8-30
# @Desc  :
from django.db.models import Q
from menu.models import  Menu
menulist=Menu.objects.filter(parent_id=0)
submenulist = Menu.objects.filter(~Q(parent_id=0))