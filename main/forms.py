#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : forms.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-8-28
# @Desc  :
from django import forms
class userForm(forms.Form):
    username=forms.CharField(label=("用户名"),max_length=100,widget=forms.TextInput(attrs={'placeholder':'aaaaaaa'}))
    password=forms.CharField(label=("密码"),widget=forms.PasswordInput)

