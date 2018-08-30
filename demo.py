#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : demo.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-8-2
# @Desc  :
from aliyunsdkcore import client
from aliyunsdkcms.request.v20180308 import QueryMetricDataRequest
from aliyunsdkecs.request.v20140526 import DescribeRegionsRequest
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkcore.profile import region_provider
import MySQLdb, datetime
import json


class Metric(object):
    def __init__(self, instanceid="", region="", accessid="", accesskey=""):
        self.instanceid = instanceid
        self.region = region
        self.accessid = accessid
        self.accesskey = accesskey
        self.container = {}

    def get_resource(self, resourceType=""):
        print
        "RegionId:%s InstanceId:%s" % (self.region, self.instanceid)
        yestoday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
        global today
        today = datetime.date.today().strftime('%Y-%m-%d 00:00:00')

        clt = client.AcsClient(self.accessId, self.accessKey, self.region)
        request = QueryMetricDataRequest.QueryMetricDataRequest()
        request.set_accept_format('json')

        request.add_query_param('Project', 'acs_ecs_dashboard')
        request.add_query_param('Metric', resourceType)
        request.add_query_param('StartTime', yestoday)
        request.add_query_param('EndTime', today)
        request.add_query_param('Dimensions', '{"instanceId":"%s"}' % self.instanceid)
        request.add_query_param('Period', '86400')

        # 发起请求
        response = clt.do_action(request)
        result = json.loads(response)
        if 'Datapoints' in result:
            datapoints = result['Datapoints']
        else:
            datapoints = ''

        if datapoints != '' and len(json.loads(datapoints)) > 0:
            self.container[resourceType] = {}
            result = json.loads(datapoints)[0]
            if type(result['Average']) == float:
                Average = str(result['Average']).split('.')[0] + '.' + str(result['Average']).split('.')[1][0:2]
            else:
                Average = result['Average']
            if type(result['Maximum']) == float:
                Maximum = str(result['Maximum']).split('.')[0] + '.' + str(result['Maximum']).split('.')[1][0:2]
            else:
                Maximum = result['Maximum']
            self.container[resourceType]['Average'] = float(Average)
            self.container[resourceType]['Maximum'] = float(Maximum)
        else:
            self.container[resourceType] = {}
            self.container[resourceType]['Average'] = 0
            self.container[resourceType]['Maximum'] = 0

        print
        "=== " * 10

    def save_data(self):
        conn = MySQLdb.connect(host='172.16.80.114', port=3306, user='root', passwd='Aa123456', charset='utf8',
                               db='novaops')
        sql = "insert into aliyun_metric(instance_id,cpu_avg,cpu_max,mem_avg,mem_max,iops_avg,iops_max,writeiops_avg,writeiops_max,network_avg,network_max,load_avg,load_max,created)values('%s',%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,'%s')" % (
            self.instanceId, float(self.container['cpu_total']['Average']),
            float(self.container['cpu_total']['Maximum']),
            float(self.container['memory_usedutilization']['Average']),
            float(self.container['memory_usedutilization']['Maximum']),
            float(self.container['disk_readiops']['Average']),
            float(self.container['disk_readiops']['Maximum']), float(self.container['disk_writeiops']['Average']),
            float(self.container['disk_writeiops']['Maximum']), float(self.container['networkout_rate']['Average']),
            float(self.container['networkout_rate']['Maximum']), float(self.container['load_15m']['Average']),
            float(self.container['load_15m']['Maximum']), today)

        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()


def getRegion():
    clt = client.AcsClient('LTAImtKD9oSsQJyQ', 'xazFiaIri1fHXDoPFV2yPtZIsnQXRy')
    request = DescribeRegionsRequest.DescribeRegionsRequest()
    request.set_accept_format('json')
    response = clt.do_action(request)
    result = json.loads(response)
    regionList = []
    for region in result['Regions']['Region']:
        regionList.append(region['RegionId'])

    return regionList


def getInstanceId(regionId):
    clt = client.AcsClient('LTAImtKD9oSsQJyQ', 'xazFiaIri1fHXDoPFV2yPtZIsnQXRy', regionId)
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
    conn = MySQLdb.connect(host='172.16.80.114', port=3306, user='root', passwd='Aa123456', charset='utf8',
                           db='novaops')

    regions = getRegion()
    print regions
    for region in regions:
        instances = getInstanceId(region)
        for instance in instances:
            metric = Metric(instance, region, 'LTAImtKD9oSsQJyQ', 'xazFiaIri1fHXDoPFV2yPtZIsnQXRy')
            metric.get_resource('cpu_total')
            metric.get_resource('memory_usedutilization')
            metric.get_resource('disk_readiops')
            metric.get_resource('disk_writeiops')
            metric.get_resource('networkout_rate')
            metric.get_resource('load_15m')
            metric.save_data()
    conn.commit()
    conn.close()
