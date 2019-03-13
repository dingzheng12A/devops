from django.shortcuts import render
from django.views.decorators.csrf import  csrf_protect,csrf_exempt
from django.contrib.auth.decorators import  login_required
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import  ContentType
from monitor.models import Monitor
import json


# Create your views here.
from .forms import  MenuForm
from .forms import SubmenuForm
from .forms import EditmenuForm
from .models import  Menu


@login_required
@csrf_protect
def addmenu(request):
    if request.method == 'POST':
        form=MenuForm(request.POST)
        if form.is_valid():
            menuname = form.cleaned_data.get('menuname')
            url = form.cleaned_data.get('menuname')
        submenuform = SubmenuForm(request.POST)
        if submenuform.is_valid():
            parent_name = submenuform.cleaned_data.get('parentname')
            parent_id = submenuform.cleaned_data.get('parentid')
            submenu_name = submenuform.cleaned_data.get('menuname')
            sub_url = submenuform.cleaned_data.get('url')

        editmenuform = EditmenuForm(request.POST)
        if editmenuform.is_valid():
            submenu_name = editmenuform.cleaned_data.get('menuname')
            sub_url = editmenuform.cleaned_data.get('url')


    else:
        form=MenuForm()
        submenuform = SubmenuForm()
        editmenuform = EditmenuForm()
        menuname=None
        url=None
        parent_name=None
        parent_id=None
        submenu_name=None
        sub_url=None

    if menuname is not None and url is not None:
        menu=Menu.objects.filter(name=menuname)
        if len(menu):
            pass
        else:
            menu=Menu.objects.create(name=menuname,parent_id=0,url=url)


    menulist=Menu.objects.filter(parent_id=0)
    submenulist = Menu.objects.filter(~Q(parent_id=0))



    # return render(request, 'dist/menu.html', dict(displayMenu='block', mainmenu=u'菜单管理', submenu=u'添加菜单',form=form,menulist=menulist,submenulist=submenulist,submenuform=submenuform,editmenuform=editmenuform))
    return render(request, 'dist/menu.html', locals())




@login_required
@csrf_protect
def addsubmenu(request):
    if request.method=='POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menuname = form.cleaned_data.get('menuname')
            url = form.cleaned_data.get('menuname')
        submenuform = SubmenuForm(request.POST)
        if submenuform.is_valid():
            parent_name = submenuform.cleaned_data.get('parentname')
            parent_id = submenuform.cleaned_data.get('parentid')
            submenu_name = submenuform.cleaned_data.get('menuname')
            sub_url = submenuform.cleaned_data.get('url')

        editmenuform = EditmenuForm(request.POST)
        if editmenuform.is_valid():
            menuname = editmenuform.cleaned_data.get('menuname')
            url = editmenuform.cleaned_data.get('url')


    else:
        form = MenuForm()
        submenuform = SubmenuForm()
        editmenuform = EditmenuForm()
        menuname = None
        url = None
        parent_name = None
        parent_id = None
        submenu_name = None
        sub_url = None

    if parent_id is not None:
        menu = Menu.objects.filter(name=submenu_name)
        if len(menu):
            pass
        else:
            menu = Menu.objects.create(name=submenu_name, parent_id=parent_id, url=sub_url)



    menulist=Menu.objects.filter(parent_id=0)
    submenulist=Menu.objects.filter(~Q(parent_id=0))

    return render(request, 'dist/menu.html', dict(displayMenu='block', mainmenu=u'菜单管理', submenu=u'添加菜单',menulist=menulist,submenulist=submenulist,form=form,submenuform=submenuform,editmenuform=editmenuform))

@login_required
@csrf_protect
def delmenu(request):
    if request.method == 'POST':
        try:
            menuname=request.POST.get('menuname')
            menu=Menu.objects.get(name=menuname)
            menu.delete()
            return HttpResponse(json.dumps({'result':1}), content_type='application/json')
        except:
            return HttpResponse(json.dumps({'result': 0}), content_type='application/json')

    else:
        return HttpResponse('')


def editmenu(request):
    if request.method == 'POST':
        try:
            menu_id=request.POST.get('menu_id')
            menuname=request.POST.get('menuname')
            url=request.POST.get('url')
            menu=Menu.objects.get(id=menu_id)
            menu.name=menuname
            menu.url=url
            menu.save()
            return HttpResponseRedirect('/menumanager/addmenu')
        except Exception as e:
            print("has an error:%s" % str(e))
            return HttpResponse(json.dumps({'result':0}),content_type='application/json')




