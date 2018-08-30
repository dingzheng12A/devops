#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : forms.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-8-29
# @Desc  :
from django import forms

class MenuForm(forms.Form):
    menuname=forms.CharField(label=u'菜单名称',max_length=50,widget=forms.TextInput(attrs={'class':'form-control col-md-6 form-control-lg','placeholder':'定义菜单名称'}))
    url=forms.CharField(label=u'超级链接',max_length=200,widget=forms.TextInput(attrs={'class':'form-control col-md-6 form-control-lg','placeholder':'定义超级链接'}))


class SubmenuForm(forms.Form):
    parentname=forms.CharField(label=u'主菜单名称',max_length=50,required=False,widget=forms.TextInput(attrs={'class':'form-control col-md-6 form-control-lg',"readonly":"true"}))
    parentid=forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}),required=False)
    menuname=forms.CharField(label=u'菜单名称',max_length=50,required=True,widget=forms.TextInput(attrs={'class':'form-control col-md-6 form-control-lg','placeholder':'定义菜单名称'}))
    url=forms.CharField(label=u'超级链接',max_length=200,required=True,widget=forms.TextInput(attrs={'class':'form-control col-md-6 form-control-lg','placeholder':'定义超级链接'}))



