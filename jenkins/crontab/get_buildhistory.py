#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : get_buildhistory.py.py
# @Author: dingzhengchunqiu
# @Date  : 18-10-30
# @Desc  :

import datetime
from jenkinsapi import jenkins
import django
import os




os.environ.setdefault("DJANGO_SETTINGS_MODULE",(os.path.dirname((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"/Devops/Devops.settings"))
django.setup()
from jenkins.models import Buildhistory
server=jenkins.Jenkins('http://172.16.80.50','admin','admin')
for jobname in server.get_jobs_list():
    job=server.get_job(jobname)
    for buildid in job.get_build_ids():
        jobinfo=job.get_build(buildid)
        print("duration:",jobinfo.get_duration())
        if not Buildhistory.objects.filter(jobname=jobname,parameters=jobinfo.get_params(),buildresult=jobinfo.get_status(),buildid=buildid):
            #item=Buildhistory.objects.create(jobname=jobname,parameters=jobinfo.get_params(),buildresult=jobinfo.get_status(),starttime=(jobinfo.get_timestamp()+datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"),buildid=buildid)
            item=Buildhistory.objects.create(jobname=jobname,parameters=jobinfo.get_params(),buildresult=jobinfo.get_status(),starttime=(jobinfo.get_timestamp()+datetime.timedelta(hours=8)).strftime("%Y-%m-%d 00:00:00"),buildid=buildid)
            item.save()
        else:
            pass

