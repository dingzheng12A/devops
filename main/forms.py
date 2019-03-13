#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : forms.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-8-28
# @Desc  :
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class userForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=100, widget=forms.TextInput(attrs={'placeholder': '用户名'}))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={'placeholder': '用户密码'}))


class UserModifyForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=30, widget=forms.TextInput(
        attrs={'placeholder': "用户名", "class": "form-control"}
    ))
    password = forms.CharField(label="密码", max_length=30, widget=forms.PasswordInput(
        attrs={'placeholder': "用户密码", "class": "form-control"}
    ))
    password_2 = forms.CharField(label="确认密码", max_length=30, widget=forms.PasswordInput(
        attrs={'placeholder': "确认密码", "class": "form-control"}
    ))

    def clean_password_2(self):
        password = self.cleaned_data.get("password")
        password_2 = self.cleaned_data.get("password_2")
        if password != password_2:
            raise ValidationError("两次输入的密码不一致")


class UserCreateForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=30, widget=forms.TextInput(
        attrs={'placeholder': "用户名", "class": "form-control", "class": "form-control"}
    ))
    email = forms.EmailField(label="电子邮件",
                             widget=forms.EmailInput(attrs={"placeholder": "电子邮件", "class": "form-control"}))
    password = forms.CharField(label="密码", max_length=30, widget=forms.PasswordInput(
        attrs={'placeholder': "用户密码", "class": "form-control"}
    ))


class GroupCreateForm(forms.Form):
    groupname = forms.CharField(label="角色名称", max_length=30, widget=forms.TextInput(
        attrs={'placeholder': "角色名称", "class": "form-control", "class": "form-control"}
    ))
    description = forms.CharField(label="描述信息", max_length=30, widget=forms.TextInput(
        attrs={'placeholder': "角色名称", "class": "form-control", "class": "form-control"}
    ))