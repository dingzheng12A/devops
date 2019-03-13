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
    url(r'^logout/', views.logout),
    #用户管理
    url(r'^modifyuser', views.modify_user, name='modify_user'),
    url(r'^check_user', views.is_user_exists, name='check_user'),
    url(r'^usermanager', views.user_manager, name='user_manager'),
    url(r'^uploadimage', views.upload_image, name='upload_image'),
    url(r'^delete_users', views.batch_delete_user, name='batch_delete_user'),
    #组管理
    # 添加组和删除组
    url(r'^groupmanager', views.group_manager, name='group_manager'),
    # 检查组是否已存在
    url(r'^check_group', views.is_group_exists, name='check_group'),
    # 将用户加入到角色
    url(r'assigin',views.assign_to,name='assigin_user_to_role'),
    url(r'query_users', views.query_users, name='query_users')
]
