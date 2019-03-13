from django.shortcuts import render
from menu.models import Menu
from jenkins.models import Buildhistory
from django.db.models import Q, Sum, Count

# Create your views here.


def jenkins_analyze(request):
    menulist = Menu.objects.filter(parent_id=0)
    submenulist = Menu.objects.filter(~Q(parent_id=0))
    buildcounts = Buildhistory.objects.values_list(
        "jobname").annotate(counts=Count(1))
    successcounts = Buildhistory.objects.filter(
        buildresult="SUCCESS").values_list("jobname").annotate(
        counts=Count(1))
    failurecounts = Buildhistory.objects.filter(
        buildresult="FAILURE").values_list("jobname").annotate(
        counts=Count(1))
    abortedcounts = Buildhistory.objects.filter(
        buildresult="ABORTED").values_list("jobname").annotate(
        counts=Count(1))
    results = []
    i = 0
    for count in buildcounts:
        row = {}
        row['jobname'] = count[0]
        row['buildcounts'] = count[1]
        for icount in successcounts:
            if icount[0] == row['jobname']:
                row['successcounts'] = icount[1]
        for icount in failurecounts:
            if icount[0] == row['jobname']:
                row['failurecounts'] = icount[1]
        for icount in abortedcounts:
            if icount[0] == row['jobname']:
                row['abortedcounts'] = icount[1]
        i = i + 1
        results.append(row)
    # print("results:",results)
    return render(request, template_name="dist/jenkins.html", context=locals())


def jenkins_chart(request):
    if 'jobname' in request.GET:
        jobname = request.GET.get("jobname")
    else:
        jobname = ""
    if "starttime" in request.GET:
        starttime = request.GET.get("starttime")
    else:
        starttime = ""
    if "endtime" in request.GET:
        endtime = request.GET.get("endtime")
    else:
        endtime = ""
    if starttime != "" and endtime != "":
        print("starttime:%s endtime:%s" % (starttime, endtime))
        buildday = Buildhistory.objects.filter(
            jobname=jobname,
            starttime__gte=starttime,
            starttime__lt=endtime).order_by("starttime").values("starttime").distinct()
        print("buildday:%s" % buildday)
        buildcounts = Buildhistory.objects.filter(
            jobname=jobname,
            starttime__gte=starttime,
            starttime__lt=endtime).order_by("starttime").values_list(
            "jobname",
            "starttime").annotate(
            counts=Count(1)).values(
                "starttime",
            "counts")
        successcounts = Buildhistory.objects.filter(
            jobname=jobname,
            buildresult="SUCCESS",
            starttime__gte=starttime,
            starttime__lt=endtime).order_by("starttime").values_list(
            "jobname",
            "starttime").annotate(
            counts=Count(1)).values(
                "starttime",
            "counts")
        failurecounts = Buildhistory.objects.filter(
            jobname=jobname,
            buildresult="FAILURE",
            starttime__gte=starttime,
            starttime__lt=endtime).order_by("starttime").values_list(
            "jobname",
            "starttime").annotate(
            counts=Count('buildresult')).values(
                "starttime",
            "counts")
        abortedcounts = Buildhistory.objects.filter(
            jobname=jobname,
            buildresult="ABORTED",
            starttime__gte=starttime,
            starttime__lt=endtime).order_by("starttime").values_list(
            "jobname",
            "starttime").annotate(
            counts=Count(1)).values(
                "starttime",
            "counts")
    else:
        buildday = Buildhistory.objects.filter(jobname=jobname).order_by(
            "starttime").values("starttime").distinct()
        buildcounts = Buildhistory.objects.filter(
            jobname=jobname).order_by("starttime").values_list(
            "jobname",
            "starttime").annotate(
            counts=Count(1)).values(
                "starttime",
            "counts")
        successcounts = Buildhistory.objects.filter(
            jobname=jobname,
            buildresult="SUCCESS").order_by("starttime").values_list(
            "jobname",
            "starttime").annotate(
            counts=Count(1)).values(
                "starttime",
            "counts")
        failurecounts = Buildhistory.objects.filter(
            jobname=jobname,
            buildresult="FAILURE").order_by("starttime").values_list(
            "jobname",
            "starttime").annotate(
            counts=Count('buildresult')).values(
                "starttime",
            "counts")
        abortedcounts = Buildhistory.objects.filter(
            jobname=jobname,
            buildresult="ABORTED").order_by("starttime").values_list(
            "jobname",
            "starttime").annotate(
            counts=Count(1)).values(
                "starttime",
            "counts")

    buildday = [s.get('starttime').strftime('%Y-%m-%d') for s in buildday]

    successCounts = []
    for i in range(len(buildcounts)):
        successCounts.append(0)
    failureCounts = []
    for i in range(len(buildcounts)):
        failureCounts.append(0)
    abortedCounts = []
    for i in range(len(buildcounts)):
        abortedCounts.append(0)

    for success in successcounts:
        for i in range(len(buildcounts)):
            if success['starttime'] == buildcounts[i]['starttime']:
                successCounts[i] = success['counts']

    for failure in failurecounts:
        for i in range(len(buildcounts)):
            if failure['starttime'] == buildcounts[i]['starttime']:
                failureCounts[i] = failure['counts']

    for aborted in abortedcounts:
        for i in range(len(buildcounts)):
            if aborted['starttime'] == buildcounts[i]['starttime']:
                abortedCounts[i] = aborted['counts']

    buildCounts = [s['counts'] for s in buildcounts]
    menulist = Menu.objects.filter(parent_id=0)
    print("buildCounts:", buildCounts, "successCounts:", successCounts)
    return render(
        request, template_name="dist/jenkins_chart.html", context=locals())
