#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : forms.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-8-29
# @Desc  :
from django import forms


class RoleSearch(forms.Form):
    rolename = forms.CharField(label='角色名称', max_length=50)
