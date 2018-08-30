#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : forms.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-8-29
# @Desc  :
from django import forms


class UserSearch(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
