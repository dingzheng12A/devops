from django.shortcuts import render
from Account.models import  Coststatistics
from menu.models import  Menu
from django.db.models import Q
from django.db.models import Sum
import pymysql




def getCost():
    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='devops', password='devops', charset='utf8', db='Devops')
    # cursor = conn.cursor()
    # SQL="select t.BillingCycle,sum(t.PayAsYouGoCost) as PayAsYouGoCost ,sum(t.SubscriptionCost) as SubscriptionCost from (select BillingCycle,case when SubscriptionType='PayAsYouGo' THEN sum(PaymentAmount) ELSE 0 END PayAsYouGoCost,case when SubscriptionType='Subscription' THEN sum(PaymentAmount) ELSE 0 END SubscriptionCost from Account_coststatistics group by SubscriptionType,BillingCycle) t group by t.BillingCycle ;"
    # cursor.execute(SQL)
    # results=[]
    # for res in cursor:
    #     row={}
    #     row['BillingCycle']=res[0]
    #     row['PayAsYouGoCost']=res[1]
    #     row['SubscriptionCost'] = res[2]
    #     results.append(row)
    #
    # return results
    Subscriptioncost = Coststatistics.objects.filter(SubscriptionType='Subscription').order_by(
        'BillingCycle').values_list('BillingCycle').annotate(allpayment=Sum('PaymentAmount'))

    PayAsYouGocost = Coststatistics.objects.filter(SubscriptionType='PayAsYouGo').order_by('BillingCycle').values_list(
        'BillingCycle').annotate(
        allpayment=Sum('PaymentAmount'))
    results = []
    i = 0
    for cost in Subscriptioncost:
        row = {}
        row['BillingCycle'] = cost[0]
        row['PayAsYouGoCost'] = round(cost[1], 2)
        row['SubscriptionCost'] = round(PayAsYouGocost[i][1], 2)
        i = i + 1
        results.append(row)
    return results


# Create your views here.

def Billing(request):
    # results=getCost()
    # BillingCycle=[billing.get('BillingCycle').strip('-')[-1]+u'月' for billing in results]
    # PayAsYouGoCost = [billing.get('PayAsYouGoCost') for billing in results]
    # SubscriptionCost = [billing.get('SubscriptionCost') for billing in results]
    submenulist = Menu.objects.filter(~Q(parent_id=0))
    menulist = Menu.objects.filter(parent_id=0)
    results = getCost()
    print("results:%s" % results)
    PayAsYouGoCost = [billing.get('PayAsYouGoCost') for billing in results]
    SubscriptionCost = [billing.get('SubscriptionCost') for billing in results]
    print("PayAsYouGoCost:%s" % PayAsYouGoCost)
    return render(request,'dist/Billing.html',context={'PayAsYouGoCost':PayAsYouGoCost,'SubscriptionCost':SubscriptionCost,"menulist":menulist,"submenulist":submenulist})
