#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main_zone.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-9-12
# @Desc  :
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test1.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-9-11
# @Desc  :

from uuid import uuid1
import hmac
import hashlib
import base64
import time
import logging
import json
import socket
import urllib
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S", filename='/var/log/privatezone.log', filemode='a')

timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def percent_encode(encodestr):
    encodestr = str(encodestr)
    res = urllib.quote(encodestr,safe="+*~")
    # res = res.replace('+', '%20')
    # res = res.replace('*', '%2A')
    # res = res.replace('%7E', '~')
    return res


def sign(parameters):
    sortedParameters = sorted(parameters.items(), key=lambda parameter: parameter[0])
    canonicalizedQueryString = ''
    for (k, v) in sortedParameters:
        canonicalizedQueryString += '&' + percent_encode(k) + '=' + percent_encode(v)
    stringToSign = 'GET&%2F&' + percent_encode(canonicalizedQueryString[1:])  # 使用get请求方法
    bs = ALIYUN_ACCESS_KEY_SECRET + '&'
    bs = bytes(bs)
    stringToSign = bytes(stringToSign)
    h = hmac.new(bs, stringToSign, hashlib.sha1)
    # 进行编码
    signature = base64.b64encode(h.digest()).strip()
    return signature


class Privatezone():
    def __init__(self, Baseurl="https://pvtz.aliyuncs.com/?", Format="xml", Version="2018-01-01",
                 SignatureVersion="1.0", SignatureMethod="HMAC-SHA1", AccessKeyId="", Timestamp=timestamp,
                 SignatureNonce=uuid1(), Action="", ZoneId="",SecurityToken=""):
        self.Baseurl = Baseurl
        self.Format = Format
        self.Version = Version
        self.SignatureVersion = SignatureVersion
        self.SignatureMethod = SignatureMethod
        self.AccessKeyId = AccessKeyId
        self.Timestamp = Timestamp
        self.SignatureNonce = SignatureNonce
        self.Action = Action
        self.ZoneId = ZoneId
        self.SecurityToken=SecurityToken

    def getrecord(self, IP=""):
        paramsinfo = {
            'Format': 'json',
            'Version': '2018-01-01',
            'SignatureMethod': 'HMAC-SHA1'
        }
        paramsinfo['SignatureNonce'] = self.SignatureNonce
        paramsinfo['SignatureVersion'] = self.SignatureVersion
        paramsinfo['SignatureMethod'] = self.SignatureMethod
        paramsinfo['AccessKeyId'] = self.AccessKeyId
        paramsinfo['Timestamp'] = self.Timestamp
        paramsinfo['Version'] = self.Version
        paramsinfo['Action'] = self.Action
        paramsinfo['ZoneId'] = self.ZoneId  # 你阿里云的机器人实例id


        paramsinfo['SecurityToken'] = self.SecurityToken
        paramsinfo['Signature'] = sign(paramsinfo)
        sortedParameters = sorted(paramsinfo.items(), key=lambda param: param[0])
        try:
            url = self.Baseurl + urllib.urlencode(sortedParameters)
            r = urllib.urlopen(url)
            print("url:%s" % url)
            records = json.loads(r.read())
            Records = records.get("Records").get("Record")
        except Exception as e:
            print("has an error:%s" % str(e))
        for record in Records:
            if IP == record.get("Value"):
                return record.get('RecordId')
        else:
            return ''

    def addrecord(self, Rr="", Type="A", Ttl=60, Value=""):
        paramsinfo = {}
        paramsinfo['SignatureNonce'] = self.SignatureNonce
        paramsinfo['SignatureVersion'] = self.SignatureVersion
        paramsinfo['SignatureMethod'] = self.SignatureMethod
        paramsinfo['AccessKeyId'] = self.AccessKeyId
        paramsinfo['Timestamp'] = self.Timestamp
        paramsinfo['Version'] = self.Version
        paramsinfo['Action'] = self.Action
        paramsinfo['ZoneId'] = self.ZoneId  # 你阿里云的机器人实例id
        paramsinfo['Rr'] = Rr
        paramsinfo['Type'] = Type
        paramsinfo['Ttl'] = Ttl
        paramsinfo['Value'] = Value
        paramsinfo['SecurityToken'] = self.SecurityToken
        paramsinfo['Signature'] = sign(paramsinfo)
        sortedParameters = sorted(paramsinfo.items(), key=lambda D: D[0])
        url = self.Baseurl + urllib.urlencode(sortedParameters)
        urllib.urlopen(url)

    def updaterecord(self, Rr="", Type="A", Ttl=60, Value="", RecordId=""):
        paramsinfo = {'Format': 'json', 'Version': self.Version, 'SignatureMethod': self.SignatureMethod,
                      'SignatureNonce': self.SignatureNonce, 'SignatureVersion': self.SignatureVersion,
                      'AccessKeyId': self.AccessKeyId, 'Timestamp': self.Timestamp, 'Action': self.Action,
                      'ZoneId': self.ZoneId,
                      'RecordId': RecordId, 'Rr': Rr, 'Type': Type, 'Ttl': Ttl, 'Value': Value}
        paramsinfo['SecurityToken']=self.SecurityToken
        paramsinfo['Signature'] = sign(paramsinfo)
        sortedParameters = sorted(paramsinfo.items(), key=lambda param: param[0])
        url = self.Baseurl + urllib.urlencode(sortedParameters)
        r = urllib.urlopen(url)
        records = json.loads(r.read())


def gethostname():
    hostname = socket.gethostname()
    return hostname


def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 53))
        ip = s.getsockname()[0]
        return ip
    finally:
        s.close()


def main(ZoneId="", AccessKeyId="",SecurityToken=""):
    hostname = gethostname()
    ipaddr = getip()
    Rt = hostname + '_' + ".".join(ipaddr.split(".")[2:4])
    DNS = Privatezone(Format="json", Action="DescribeZoneRecords", ZoneId=ZoneId, AccessKeyId=AccessKeyId,SecurityToken=SecurityToken)
    recordId = DNS.getrecord(IP=ipaddr)
    if recordId == '':
        try:
            DNS = Privatezone(Action="AddZoneRecord", ZoneId=ZoneId, AccessKeyId=AccessKeyId,SecurityToken=SecurityToken)
            DNS.addrecord(Rt, "A", 60, ipaddr)
            logging.info("ZoneId:{} add record success: {} {} {}".format(ZoneId, Rt, 'A', ipaddr))
        except Exception as e:
            logging.error("ZoneId:{} add record failure: {} {} {}".format(
                str(ZoneId), Rt, 'A', ipaddr))
    else:
        try:
            DNS = Privatezone(Action="UpdateZoneRecord", ZoneId=ZoneId, AccessKeyId=AccessKeyId,SecurityToken=SecurityToken)

            DNS.updaterecord(Rt, "A", 60, ipaddr, recordId)
            logging.info("ZoneId:{} update record success: {} {} {}".format(ZoneId, Rt, 'A', ipaddr))
        except Exception:
            logging.error("ZoneId:{} update record failure: {} {} {}".format(ZoneId, Rt, 'A', ipaddr))


if __name__ == '__main__':
    # ALIYUN_ACCESS_KEY_ID = "LTAImtKD9oSsQJyQ"
    # ALIYUN_ACCESS_KEY_SECRET = "xazFiaIri1fHXDoPFV2yPtZIsnQXRy"
    url="http://100.100.100.200/latest/meta-data/Ram/security-credentials/EcsUpdatePrivateZoneRecord"
    r = urllib.urlopen(url)
    credentials=json.loads(r.read())
    ALIYUN_ACCESS_KEY_ID=credentials.get('AccessKeyId')
    ALIYUN_ACCESS_KEY_SECRET=credentials.get('AccessKeySecret')
    SecurityToken=credentials.get('SecurityToken')
    print("ALIYUN_ACCESS_KEY_ID:%s ALIYUN_ACCESS_KEY_SECRET:%s SecurityToken:%s" %(ALIYUN_ACCESS_KEY_ID,ALIYUN_ACCESS_KEY_SECRET,SecurityToken))
    ZoneId = sys.argv[1]
    main(ZoneId, ALIYUN_ACCESS_KEY_ID,SecurityToken)
