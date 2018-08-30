#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : aliyun.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-8-22
# @Desc  :

# !/usr/bin/env python
# coding=utf-8
# 功能介绍
# 获取阿里云ecs性能统计信息并存储至mysql数据库
# Created:2018-07-31
# Author:hexing
from aliyunsdkcore import client
from aliyunsdkcms.request.v20180308 import QueryMetricDataRequest
from aliyunsdkecs.request.v20140526 import DescribeRegionsRequest
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
import MySQLdb, datetime
import json
import config


class Metric(object):
    def __init__(self, instance_id="", region="", access_id=config.ALIYUN_ID, access_key=config.ALIYUN_SECRET):
        self.instanceId = instance_id
        self.region = region
        self.accessId = access_id
        self.accessKey = access_key
        self.container = {}

    def get_resource(self, resource_type=""):
        print
        "RegionId:%s InstanceId:%s" % (self.region, self.instanceId)
        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
        global today
        today = datetime.date.today().strftime('%Y-%m-%d 00:00:00')

        clt = client.AcsClient(self.accessId, self.accessKey, self.region)
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')

        request.add_query_param('Project', 'acs_ecs_dashboard')
        request.add_query_param('Metric', resource_type)
        request.add_query_param('StartTime', yesterday)
        request.add_query_param('EndTime', today)
        request.add_query_param('Dimensions', '{"instanceId":"%s"}' % self.instanceId)
        request.add_query_param('Period', '86400')

        # 发起请求
        response = clt.do_action(request)
        result = json.loads(response)
        if result.has_key('Datapoints'):
            datapoints = result['Datapoints']
        else:
            datapoints = ''
        print
        "Datapoints:%s type:%s" % (datapoints, type(datapoints))
        # result=json.loads(Datapoints)
        # print "type of result:%s" %(type(result))
        if datapoints != '' and len(json.loads(datapoints)) > 0:
            self.container[resource_type] = {}
            result = json.loads(datapoints)[0]
            if type(result['Average']) == float:
                average = str(result['Average']).split('.')[0] + '.' + str(result['Average']).split('.')[1][0:2]
            else:
                average = result['Average']
            if type(result['Maximum']) == float:
                maximum = str(result['Maximum']).split('.')[0] + '.' + str(result['Maximum']).split('.')[1][0:2]
            else:
                maximum = result['Maximum']
            self.container[resource_type]['Average'] = float(average)
            self.container[resource_type]['Maximum'] = float(maximum)
        else:
            self.container[resource_type] = {}
            self.container[resource_type]['Average'] = 0
            self.container[resource_type]['Maximum'] = 0
        print
        "=== " * 10

    def save_data(self):
        conn = MySQLdb.connect(host=config.SQL_HOST, port=config.SQL_PORT, user=config.SQL_USER,
                               passwd=config.SQL_PASS, charset='utf8', db=config.SQL_DBNAME)
        sql = "insert into aliyun_metric(instance_id,cpu_avg,cpu_max,mem_avg,mem_max,iops_avg,iops_max," \
              "writeiops_avg,writeiops_max,network_avg,network_max,load_avg,load_max,created)" \
              "values('%s',%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,'%s')" % (
                  self.instanceId, float(self.container['cpu_total']['Average']),
                  float(self.container['cpu_total']['Maximum']),
                  float(self.container['memory_usedutilization']['Average']),
                  float(self.container['memory_usedutilization']['Maximum']),
                  float(self.container['disk_readiops']['Average']),
                  self.container['disk_readiops']['Maximum'], self.container['disk_writeiops']['Average'],
                  self.container['disk_writeiops']['Maximum'], self.container['networkout_rate']['Average'],
                  float(self.container['networkout_rate']['Maximum']), float(self.container['load_15m']['Average']),
                  float(self.container['load_15m']['Maximum']), today)
        print
        "Running SQL:%s" % sql
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()


def getRegion():
    clt = client.AcsClient(config.ALIYUN_ID, config.ALIYUN_SECRET)
    request = DescribeRegionsRequest.DescribeRegionsRequest()
    request.set_accept_format('json')
    response = clt.do_action(request)
    result = json.loads(response)
    regionList = []
    for region in result['Regions']['Region']:
        regionList.append(region['RegionId'])

    return regionList


def getInstanceId(regionId):
    clt = client.AcsClient(config.ALIYUN_ID, config.ALIYUN_SECRET)
    request = DescribeInstancesRequest.DescribeInstancesRequest()
    request.set_accept_format('json')
    request.add_query_param('RegionId', regionId)
    request.add_query_param('PageSize', 100)
    request.add_query_param('PageNumber', 1)
    response = clt.do_action(request)
    results = json.loads(response)['Instances']['Instance']
    instanceList = []
    for result in results:
        instanceList.append(result['InstanceId'])
    return instanceList


if __name__ == '__main__':
    conn = MySQLdb.connect(host=config.SQL_HOST, port=config.SQL_PORT, user=config.SQL_USER,
                           passwd=config.SQL_PASS, charset='utf8', db=config.SQL_DBNAME)
    regions = getRegion()
    print
    regions
    for region in regions:
        if region in ['ap-northeast-1', 'eu-central-1']:
            instances = getInstanceId(region)
            region = 'cn-hangzhou'
        else:
            instances = getInstanceId(region)

        for instance in instances:
            metric = Metric(instance, region, 'LTAImtKD9oSsQJyQ', 'xazFiaIri1fHXDoPFV2yPtZIsnQXRy')
            metric.get_resource('cpu_total')
            metric.get_resource('memory_usedutilization')
            metric.get_resource('disk_readiops')
            metric.get_resource('disk_writeiops')
            metric.get_resource('networkout_rate')
            metric.get_resource('load_15m')
            # metric.save_data()
    conn.commit()
    conn.close()
