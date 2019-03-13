#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : export_month.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-9-28
# @Desc  :

# !/usr/bin/env python
# coding:utf-8
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from smtplib import SMTP
from email import encoders
from time import sleep
import xlsxwriter
import MySQLdb
import datetime
import os
import re
import sys
import redis


# r=redis.ConnectionPool(host='localhost',port=6379,db=0,password='')


def analysis(product="", country=""):
    sql = "SELECT a.enterprisename as '公司名称',a.enterpriseid as '组织id',a.user_nums '用户数',a.terminal_nums '终端数',a.sync_nums '同步终端数',a.async_nums '异步终端数',a.user_nums-b.user_nums '新增用户',a.sync_nums-b.sync_nums '新增同步终端',a.async_nums-b.async_nums '新增异步终端',a.user_nums-c.user_nums '一周新增用户',a.sync_nums-c.sync_nums '>一周新增同步终端',a.async_nums-c.async_nums '一周新增异步终端' FROM " + product + "_" + country + "_detail a INNER JOIN " + product + "_" + country + "_detail b INNER JOIN " + product + "_" + country + \
        "_detail c ON a.enterpriseid = b.enterpriseid AND a.enterprisename = b.enterprisename AND a.enterpriseid = c.enterpriseid AND a.enterprisename = c.enterprisename  WHERE upper(a.enterprisename) not like 'NOVA%' and a.enterprisename not like '诺瓦%' and a.enterprisename not like '郭梦婷%'  AND datediff(date_format(a.createtime,'%Y-%m-%d'),date_format(b.createtime,'%Y-%m-%d')) = 1 and datediff(date_format(a.createtime,'%Y-%m-%d'),date_format(c.createtime,'%Y-%m-%d')) = 7 and a.createtime>=date_format(now(),'%Y-%m-%d') ORDER BY a.terminal_nums DESC;"
    sql2 = "select date_format(createtime,'%Y-%m-%d') as 日期,sum(user_nums) as 用户数,sum(terminal_nums) as 终端数,sum(sync_nums) as 同步终端数,sum(async_nums) 异步终端数 from " + \
        product + "_" + country + \
        "_detail group by date_format(createtime,'%Y-%m-%d') having 日期>date_sub(curdate(),interval 30 day) ;"
    sql3 = "select date_format(createtime,'%Y-%m-%d') as 日期,sum(user_nums) as 用户数,sum(lite_nums) as `lite终端数`,sum(sync_nums) as `pro终端数` from " + \
        product + "_" + country + \
        "_detail group by date_format(createtime,'%Y-%m-%d') having 日期>date_sub(curdate(),interval 30 day) ;"
    print "Running SQL:%s" % sql
    cursor.execute(sql)
    cursor2 = conn.cursor()
    cursor2.execute(sql2)
    if product == "vnnox":
        cursor3 = conn.cursor()
        cursor3.execute(sql3)
    if country == "jp":
        Country = u"日本"
    elif country == "eu":
        Country = u"欧洲"
    elif country == "au":
        Country = u"澳洲"
    elif country == "us":
        Country = u"美国"
    elif country == "sg":
        Country = u"新加坡"
    else:
        Country = u"中国"

    days = datetime.timedelta(days=-7)

    dateTime = datetime.datetime.now().strftime('%Y-%m-%d')
    aWeek = (datetime.datetime.now() + days).strftime('%Y-%m-%d')
    print
    "aWeek:%s" % aWeek
    bold = workbook.add_format({'bold': True})
    worksheet = workbook.add_worksheet(
        product + "_" + country + "_" + dateTime)
    worksheet1 = workbook.add_worksheet(
        product + "_" + country + dateTime + "_" + u"终端月增长趋势")
    worksheet2 = workbook.add_worksheet(
        product + "_" + country + "_" + dateTime + u"终端月增长趋势2")
    titles = [u'公司名称', u'组织Id', u'用户数', u'终端数', u'同步终端数', u'异步终端数', u'新增用户', u'新增同步终端', u'新增异步终端', u'一周新增用户',
              u'一周新增同步终端', u'一周新增异步终端']
    titles2 = [u'日期', u'用户数', u'终端数', u'同步终端数', u'异步终端数']
    titles3 = [u'日期', u'用户数', u'终端数', u'lite终端数', u'pro终端数']

    if product == "vnnox":
        i = 0
        for title in titles3:
            worksheet2.write(0, i, title, bold)
            i = i + 1

    i = 0
    for title in titles:
        worksheet.write(0, i, title, bold)
        # worksheet1.write(0, i, title, bold)
        # worksheet2.write(0, i, title, bold)
        i = i + 1
    i = 0
    for title in titles2:
        worksheet1.write(0, i, title, bold)
        i = i + 1

    h = 1
    incNum = 1
    incWeeknum = 1
    for res in cursor:
        l = 0
        # 定义增量数据的行数
        hasOne = 0
        hasOneweek = 0
        for col in res:
            if res[6] != 0 or res[7] != 0 or res[8] != 0:
                worksheet1.set_column(incNum, l, 20)
                worksheet1.write(incNum, l, col)
                hasOne = 1

            # 插入一周数据
            # if res[9] != 0 or res[10] != 0 or res[11] != 0:
            #     worksheet2.set_column(incWeeknum, l, 20)
            #     worksheet2.write(incWeeknum, l, col)
            #     hasOneweek = 1

            worksheet.set_column(h, l, 20)
            worksheet.write(h, l, col)

            l = l + 1
        incNum = incNum + hasOne
        incWeeknum = incWeeknum + hasOneweek

        h = h + 1

    # 获取总记录数
    counts = h
    print
    "current Rows is:%d" % counts
    worksheet.write(h, 0, u'汇总统计')
    # 写入用户总数
    worksheet.write_formula(h, 2, '=SUM(C2:C%s)' % h)
    # 写入终端总数
    worksheet.write_formula(h, 3, '=SUM(D2:D%s)' % h)
    worksheet.write_formula(h, 4, '=SUM(E2:E%s)' % h)
    worksheet.write_formula(h, 5, '=SUM(F2:F%s)' % h)

    # 获得总行数
    h = h + 1
    # 写入top20以外终端总数
    if counts > 20:
        top_rows = 11
    else:
        top_rows = counts

    chart = workbook.add_chart({'type': 'column', 'subtype': 'stacked'})

    if counts > 20:
        insert_rows = 21
    else:
        insert_rows = counts

    # 设置图表标题，并将标题字体颜色设置为白色
    chart.set_title({'name': u'%s%s Top20 「按照终端数排序」' % (
        product, Country), 'name_font': {'color': 'black'}})
    # for wps excel 写法
    # chart.add_series({'name': u'终端总数', 'categories': '=A2:A%s' % (insert_rows), 'values': '=D2:D%s' % (insert_rows)})
    # for wps excel 写法
    chart.add_series({'name': u'同步终端',
                      'categories': '=A2:A%s' % (insert_rows),
                      'values': '=E2:E%s' % (insert_rows)})
    # for wps excel 写法
    chart.add_series({'name': u'异步终端',
                      'categories': '=A2:A%s' % (insert_rows),
                      'values': '=F2:F%s' % (insert_rows)})
    chart.set_style(26)
    chart.set_legend({'position': 'right', 'font': {'color': 'black'}})
    chart.set_size({'width': 700, 'height': 576})
    # chart.set_plotarea({'fill': {'color': '#5B5B5B'}})
    # chart.set_chartarea({'fill': {'color': 'black'}})
    chart.set_x_axis({'num_font': {'color': 'black'}})
    chart.set_y_axis({'num_font': {'color': 'black'},
                      'name_font': {'color': 'black'}})
    chart.set_table({'show_keys': True, 'font': {'color': 'black'}})
    h = h + 2
    worksheet.insert_chart('A%s' % h, chart, {'x_offset': 25, 'y_offset': 10})

    h = 1
    incNum = 1
    incWeeknum = 1
    for res2 in cursor2:
        l = 0
        # 定义增量数据的行数
        hasOne = 0
        hasOneweek = 0
        for col in res2:
            # if res[6] != 0 or res[7] != 0 or res[8] != 0:
            worksheet1.set_column(incNum, l, 20)
            worksheet1.write(incNum, l, col)
            hasOne = 1

            worksheet1.set_column(h, l, 20)
            worksheet1.write(h, l, col)

            l = l + 1
        incNum = incNum + hasOne
        incWeeknum = incWeeknum + hasOneweek

        h = h + 1

    # 获取总记录数
    counts = h
    print "current Rows is:%d" % counts
    worksheet.write(h, 0, u'汇总统计')
    # 写入用户总数
    worksheet.write_formula(h, 2, '=SUM(C2:C%s)' % h)
    # 写入终端总数
    worksheet.write_formula(h, 3, '=SUM(D2:D%s)' % h)
    worksheet.write_formula(h, 4, '=SUM(E2:E%s)' % h)
    worksheet.write_formula(h, 5, '=SUM(F2:F%s)' % h)

    # 获得总行数
    h = h + 1
    # 写入top20以外终端总数
    if counts > 20:
        top_rows = 11
    else:
        top_rows = counts

    row = 1
    chart2 = workbook.add_chart({'type': 'line'})
    chart2.set_size({'width': 1300, 'height': 576})
    chart2.set_title({'name': u'%s%s 终端「一月增长趋势」' % (
        product, Country), 'name_font': {'color': 'black'}})
    chart2.set_y_axis({'num_font': {'color': 'black'},
                       'name_font': {'color': 'black'}})
    chart2.add_series({
        'name': u'用户',
        'categories': '=$A2:$A$%s' % (incNum),
        'values': '=$B2:$B$%s' % (incNum)})
    # chart2.set_style(12)
    chart2.set_drop_lines()
    chart2.add_series({'name': u'终端总数',
                       'categories': '=A2:A%s' % (insert_rows),
                       'values': '=C2:C$%s' % (insert_rows)})

    chart2.add_series({
        'name': u'同步终端',
        'categories': '=$A2:$A$%s' % (incNum),
        'values': '=$D2:$D$%s' % (incNum)})
    chart2.set_legend({'position': 'right', 'font': {'color': 'black'}})
    chart2.add_series({'name': u'异步终端',
                       'categories': '=$A$2:$A$%s' % (incNum),
                       'values': '=$E2:$E$%s' % (incNum)})
    chart2.set_table({'show_keys': True, 'font': {'color': 'black'}})
    # chart2.set_plotarea({'fill': {'color': '#5B5B5B'}})
    # chart2.set_chartarea({'fill': {'color': 'black'}})
    worksheet1.insert_chart('A%s' % str(incNum + 1), chart2)
    if product == 'vnnox':
        h = 1
        incNum = 1
        incWeeknum = 1
        for res3 in cursor3:
            l = 0
        # 定义增量数据的行数
            hasOne = 0
            hasOneweek = 0
            for col in res2:
                worksheet2.set_column(incNum, l, 20)
                worksheet2.write(incNum, l, col)
                hasOne = 1

                l = l + 1
            incNum = incNum + hasOne
            incWeeknum = incWeeknum + hasOneweek

            h = h + 1

    # 获取总记录数
            counts = h
            print
            "current Rows is:%d" % counts

            # 获得总行数
            h = h + 1
            # 写入top20以外终端总数
            if counts > 20:
                top_rows = 11
            else:
                top_rows = counts

            row = 1

            chart3 = workbook.add_chart({'type': 'line'})
            chart3.set_size({'width': 1300, 'height': 576})
            chart3.set_title({'name': u'%s%s lite终端和pro终端「一月增长趋势」' % (
                product, Country), 'name_font': {'color': 'white'}})
            chart3.set_y_axis({'num_font': {'color': 'white'},
                               'name_font': {'color': 'white'}})
            chart3.add_series({
                'name': u'lite版终端',
                'categories': '=$A2:$A$%s' % (incWeeknum),
                'values': '=$D2:$D$%s' % (incWeeknum)})
            chart3.set_legend(
                {'position': 'right', 'font': {'color': 'white'}})
            chart3.add_series(
                {'name': u'pro版终端', 'categories': '=$A$2:$A$%s' % (incWeeknum), 'values': '=$E2:$E$%s' % (incWeeknum)})
            chart3.set_table({'show_keys': True, 'font': {'color': 'white'}})
            chart3.set_plotarea({'fill': {'color': '#5B5B5B'}})
            chart3.set_chartarea({'fill': {'color': 'black'}})
            worksheet2.insert_chart('A%s' % str(incWeeknum + 1), chart3)

    # 插入宏
    workbook.add_vba_project(
        os.path.join(
            os.path.dirname(
                sys.argv[0]),
            './vbaProject.bin'))
    worksheet.insert_button('B100', {
        'macro': 'Sub exportimg() Dim XlsChart As ChartObject For Each XlsChart In Worksheets("%s_%s").ChartObjects XlsChart.Chart.Export Filename:="Z:\" & XlsChart.Name & ".jpg", FilterName:="JPG" Next End Sub' % (
            product, dateTime)})


def sendmail(From="", Subject="", Text="", To=[], cc="", files=[]):
    msg = MIMEMultipart()
    msg['From'] = From
    msg['Subject'] = Subject
    msg['To'] = ";".join(To)
    msg['Cc'] = cc
    msg[
        'User-Agent'] = 'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
    Content = ""
    imagePath = os.path.join(os.path.dirname(sys.argv[0]), 'image')
    for i, file in enumerate(sorted(os.listdir(imagePath), reverse=True)):
        if file.endswith(".jpg"):
            strinfo = re.compile('^[a-zA-Z]+')

            imgCountry = strinfo.sub('', file.split(' ')[0])
            Content += "【%s】" % imgCountry
            print
            "imgCount:%s,file:%s" % (i, file)
            Content += "<br><br>"
            if i % 3 == 0:
                imgCount = 1
            elif i % 3 == 1:
                imgCount = 2
            else:
                imgCount = 3
            Content += "图{count}.{number}: ".format(count=(i / 3 if i % 3 == 0 else i / 3 + 1), number=imgCount) + \
                       file.split('.')[0]
            Content += '<br>'

            Content = Content + \
                "<img align='center' src='cid:image{count}'><br>".format(
                    count=i + 2)
            image = open(os.path.join(imagePath, file), 'rb')
            msgImage = MIMEImage(image.read())
            image.close()
            Content = Content + "<br>"
            msgImage.add_header(
                'Content-ID',
                '<image{count}>'.format(
                    count=i + 2))
            msg.attach(msgImage)
            del msgImage
    Text += "<br><br>"
    Text += Content
    msg.attach(MIMEText(Text, 'html', 'utf-8'))
    for file in files:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(file, 'rb').read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            'attachment; filename="%s"' %
            os.path.basename(file))
    msg.attach(part)
    msg['Accept-Language'] = 'zh-CN'
    msg['Accept-Charset'] = 'ISO-8859-1,utf-8'
    s = SMTP('qiye163mx02.mxmail.netease.com', 25)
    s.login('swat@novastar.tech', 'vFneUMejtB381s3g')
    s.sendmail(From, To, msg.as_string())


if __name__ == "__main__":
    dateTime = datetime.datetime.now().strftime('%Y-%m-%d')
    # outfile=u"用户数据统计"+dateTime+".xlsx"
    outfile = os.path.join(
        os.path.dirname(
            sys.argv[0]),
        "image",
        "analyzer_%s.xlsm" %
        dateTime)
    workbook = xlsxwriter.Workbook(outfile)
    conn = MySQLdb.connect(host='10.20.20.18', port=3306, user='test', passwd='test', charset='utf8',
                           db='Userstatistical')
    cursor = conn.cursor()
    analysis('vnnox', 'cn')
    analysis('vnnox', 'jp')
    analysis('vnnox', 'us')
    analysis('vnnox', 'au')
    analysis('vnnox', 'eu')
    analysis('novaicare', 'cn')
    analysis('novaicare', 'sg')
    analysis('novaicare', 'us')
    workbook.close()
    cursor.close()
    print
    "已经完成excel数据生成."
    sleep(120)
    # # sendmail(From='swat@novastar.tech', Subject=u"云服务运营数据统计-%s" % dateTime,
    #          To=["handan@novastar.tech", "liuyan@novastar.tech", "tangsf@novastar.tech", "luwei@novastar.tech",
    #              "chenliang@novastar.tech", "wangwei@novastar.tech", "liyanni@novastar.tech", "ningbo@novastar.tech",
    #              "hexing@novastar.tech"], cc="hexing@novastar.tech", files=[outfile],
    #          Text="各位好，<br>以下是云服务运营数据报告，报告已更新至%s，请查阅。" % dateTime)
sendmail(
    From='swat@novastar.tech',
    Subject=u"云服务运营数据统计-%s" %
    dateTime,
    To=["hexing@novastar.tech"],
    cc="hexing@novastar.tech",
    files=[outfile],
    Text="各位好，<br>以下是云服务运营数据报告，报告已更新至%s，请查阅。" %
    dateTime)
