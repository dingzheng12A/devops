#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-9-11
# @Desc  :
import hmac
import hashlib
from base64 import b64encode
from urllib import parse
string="GET&%2F&AccessKeyId%3Dtestid&Action%3DGetDeviceInfos&AppKey%3D23267207&Devices%3De2ba19de97604f55b165576736477b74%252C92a1da34bdfd4c9692714917ce22d53d&Format%3DXML&RegionId%3Dcn-hangzhou&SignatureMethod%3DHMAC-SHA1&SignatureNonce%3Dc4f5f0de-b3ff-4528-8a89-fa478bda8d80&SignatureVersion%3D1.0&Timestamp%3D2016-03-29T03%253A59%253A24Z&Version%3D2015-08-27"

key="testsecret&"
x=hmac.new(key.encode(encoding='utf-8'),string.encode(encoding='utf-8'),digestmod=hashlib.sha1)
y=b64encode(x.digest())
print("y:%s" % parse.quote(y))