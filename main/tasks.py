#coding: utf-8
from celery import task
from celery.schedules import crontab
from Devops.settings import  BASE_LOG_DIR,DATABASES as database
import logging
import os
import pymysql
@task
def add(a, b):
    conn = pymysql.connect(host="172.16.9.119", port=3306, user="devops", password="devops",db="demo")
    cursor = conn.cursor()
    cursor.execute("insert into test(id)values(%d);" % int(a+b))
    conn.commit()
    cursor.close()
    conn.close()
    return a + b


@task
def sub(a,b):
    conn = pymysql.connect(host="172.16.9.119", port=3306, user="devops", password="devops", db="demo")
    cursor = conn.cursor()
    cursor.execute("insert into test(id)values(%d);" % int(a - b))
    conn.commit()
    cursor.close()
    conn.close()
    return a - b

@task
def hello(name=""):
    print(name)
    return "name:{name}".format(name=name)