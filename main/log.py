#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : log.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-8-2
# @Desc  :
import logging
#logging.basicConfig(file='aaa.log',level=logging.DEBUG,datefmt='%Y-%m-%d')
#logging.basicConfig(filename='app.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',datefmt='%Y-%m-%d')
logging.basicConfig(filename='aaa.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)s] %(message)s')
logging.info("aaaaaaa")