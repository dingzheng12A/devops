from django.shortcuts import render
import re
from menu.models import  Menu
from django.db.models import Q
pattern=re.compile(r' src="/upload([\s\S]*?\.png|jpg)"',re.M)

# Create your views here.
import pymysql
product_page=1
news_page=1



def get_infors(protype="news",search=""):
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='devops', password='devops', charset='utf8', db='Devops')
	cursor=conn.cursor()
	results = []

	SQL = "SELECT createtime,title,content,allcontent,img_url,id FROM spider_"+protype+" WHERE  (title like '%" + search + "%' OR content like '%" + search + "%') ORDER BY createtime desc"
	print("running sql:%s" % SQL)
	cursor.execute(SQL)
	for res in cursor:
		result={}
		result['createtime']=res[0]
		result['title']=res[1]
		result['content']=res[2]
		result['allcontent']=re.sub(pattern,r' src="/static\1"',str(res[3]))
		result['allcontent']=re.sub(r'<div class="operation">',r'<div class="operation" style="display:none">',result['allcontent'])
		result['img_url']=[]
		for img in res[4].split("|"):
			result['img_url'].append(img)
		result['id']=res[5]
		results.append(result)

	cursor.close()
	conn.close()
	return results

def main(request):
	global news_page
	global product_page
	if "news_page" in request.GET:
		news_page = int(request.GET.get("news_page"))
	elif "product_page" in request.GET:
		product_page = int(request.GET.get("product_page"))
	if "search" in request.POST:
		search=request.POST.get("search")
	else:
		search=""
	news_results=get_infors(protype="news",search=search)
	product_results=get_infors(protype="product",search=search)

	if len(news_results)%3==0:
		#news_page_range=range(1,int(len(news_results)/3)+1)
		news_max_page=int(len(news_results)/3)
	else:
		#news_page_range=range(1,int(len(news_results)/3)+2)
		news_max_page=int(len(news_results)/3)+1
	if news_max_page > 10:
		if news_page >5 and news_page+5 <= news_max_page:
			news_page_range=range(news_page-5,news_page+5)
		elif news_page+5 > news_max_page:
			news_page_range=range(news_max_page-9,news_max_page+1)
		else:
			news_page_range=range(1,11)
	else:
		news_page_range=range(1,news_max_page+1)

	if len(product_results)%3==0:
		#product_page_range=range(1,int(len(product_results)/3)+1)
		product_max_page=int(len(product_results)/3)
	else:
		#product_page_range=range(1,int(len(product_results)/3)+2)
		product_max_page=int(len(product_results)/3)+1
	if product_max_page > 10:
		if product_page >5 and product_page+5 <= product_max_page:
			product_page_range=range(product_page-5,product_page+5)
		elif product_page+5 > product_max_page:
			product_page_range=range(product_max_page-9,product_max_page+1)
		else:
			product_page_range=range(1,11)
	else:
		product_page_range=range(1,product_max_page+1)
	print("xxx product_page_range:%s.product_max_page:%s\n" % (product_page_range,product_max_page))
	menulist = Menu.objects.filter(parent_id=0)
	submenulist = Menu.objects.filter(~Q(parent_id=0))
	return render(request,'dist/kalaite.html',dict(news_contents=news_results[(news_page-1)*3:news_page*3],news_page_range=news_page_range,news_page=news_page,news_max_page=news_max_page,product_contents=product_results[(product_page-1)*3:product_page*3],product_page_range=product_page_range,product_page=product_page,product_max_page=product_max_page,menulist=menulist,submenulist=submenulist))

def tests(request):
	users=["zhangsan","lisi","wangwu"]
	return render(request,'dist/test1.html',{'a':10,'users':users})
