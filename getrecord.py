#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test1.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-9-11
# @Desc  :


import hmac
import hashlib
from urllib import parse
from urllib import request
from base64 import b64encode
# from xml.dom.minidom import
import requests
import random
import datetime
import base64
from uuid import uuid1
import time
import json


def percent_encode(encodeStr):
    encodeStr = str(encodeStr)
    res = parse.quote(encodeStr)
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res


signatureNonece = random.randint(15215528852396, 15215538852396)
utctime = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

D = {
    'Format': 'json',
    'Version': '2018-01-01',
    'SignatureMethod': 'HMAC-SHA1'
}
timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
ALIYUN_ACCESS_KEY_ID="LTAImtKD9oSsQJyQ"
ALIYUN_ACCESS_KEY_SECRET="xazFiaIri1fHXDoPFV2yPtZIsnQXRy"
D['SignatureNonce'] = str(uuid1())
D['SignatureVersion'] = 1.0
D['AccessKeyId'] = ALIYUN_ACCESS_KEY_ID
D['Timestamp'] = timestamp
D['Version']='2018-01-01'
def sign(parameters):
    sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
    print(sortedParameters)
    canonicalizedQueryString = ''
    for (k, v) in sortedParameters:
        canonicalizedQueryString += '&' + percent_encode(k) + '=' + percent_encode(v)
    stringToSign = 'GET&%2F&' + percent_encode(canonicalizedQueryString[1:])  # 使用get请求方法
    bs = ALIYUN_ACCESS_KEY_SECRET + '&'
    bs = bytes(bs, encoding='utf8')
    stringToSign = bytes(stringToSign, encoding='utf8')
    h = hmac.new(bs, stringToSign, hashlib.sha1)
    # 进行编码
    signature = base64.b64encode(h.digest()).strip()
    return signature


D['Action'] = "DescribeZoneRecords"
D['ZoneId'] = "837b63b4f860b4f595bcddd6a33397ab"  # 你阿里云的机器人实例id

D['Signature'] = sign(D)

sortedParameters = sorted(D.items(), key=lambda D: D[0])


url = 'https://pvtz.aliyuncs.com/?' + parse.urlencode(sortedParameters)
print(url)
r = requests.get(url)
print(r.text)
records=json.loads(r.text)
print("type records:%s" % type(records.get('Records')))




