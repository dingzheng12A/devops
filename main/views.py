import json
import re
import datetime
import pymysql
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db.models import Q
from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.sessions.models import Session
from .forms import userForm
from User.forms import UserSearch
from Role.forms import RoleSearch
from menu.forms import  MenuForm
from menu.menuQuery import  menulist,submenulist
from django.http import StreamingHttpResponse

regexp = re.compile('\s+')


# Create your views here.

@csrf_protect
def login(request):
    get_token(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("username:%s,password:%s" % (username, password))
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            print("user:%s" % user.username)
            auth.login(request, user)
            request.session['username'] = user.username
            result = {'result': 1}
            return HttpResponse(json.dumps(result), content_type='application/json')
        else:

            result = {'result': 0}
            return HttpResponse(json.dumps(result), content_type='application/json')
    return render_to_response('dist/login.html', csrf(request))


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponse(json.dumps({'result': 1}), content_type='application/json')

@login_required
@csrf_protect
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        password = request.POST.get('passwd')
        email = request.POST.get('email')
        try:
            user = User(username=username, email=email, first_name=nickname)
            user.set_password(password)
            user.save()
            result = {'result': 1, 'message': 'success for adduser!'}
        except Exception as e:
            print("has an error:%s", e)
            result = {'result': 0, 'message': 'failure for adduser!'}

        return HttpResponse(json.dumps(result), content_type='application/json')


@login_required
@csrf_protect
def userinfo(request):
    userlist = User.objects.exclude(username='admin')
    pagintor = Paginator(userlist, 3, 2)
    page = request.GET.get('page')
    try:
        users = pagintor.page(page)
    except PageNotAnInteger:
        users = pagintor.page(1)
    except EmptyPage:
        users = paginator.page(pagintor.num_pages)
    return HttpResponse(json.dumps(users), content_type='application/json')


@login_required
@csrf_protect
def resetpass(request):
    password = ''
    is_active = 0
    username = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        if 'pwd' in request.POST:
            password = request.POST.get('pwd')
        else:
            password = None
        if 'is_active' in request.POST:
            is_active = request.POST.get('status')
        else:
            is_active = None
    try:
        user = User.objects.filter(username=username).first()
        if password is not None:
            user.set_password(password)
        if is_active is not None:
            user.is_active = is_active
        user.save()
        print("user:%s;password:%s;encpass:%s" % (user.username, password, user.password))
        del user
        result = {'result': 1}
    except Exception as e:
        print("has an error:%s" % e)
        result = {'result': 0}
    return HttpResponse(json.dumps(result), content_type='application/json')


def monitor_resource(sql):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='devops', password='devops', charset='utf8', db='Devops')
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
    conn.close()
    return cursor.fetchall()


@login_required
@csrf_protect
def mainpage(request):
    request.session.set_expiry(0)
    print("session:%s" % dir(request.session['username']))
    now = datetime.datetime.now()
    display_dashboard = 'block'
    before_20_minute = datetime.timedelta(minutes=-20)
    first_time = (now + before_20_minute)
    session = Session.objects.all()
    sql = r"SELECT createtime,memory_used,cpu_load_5m,disk_used,memory_spare,disk_spare,cpu_load_10m,cpu_load_15m " \
          r"FROM resource_monitor WHERE CREATETIME>'%s'" % first_time.strftime(
        '%Y-%m-%d %H:%M')
    monitor_resource(sql)
    createtime = []
    memory = []
    cpu_load_5 = []
    cpu_load_10 = []
    cpu_load_15 = []
    disk = []
    memory_spare = []
    disk_spare = []
    results = monitor_resource(sql)

    for res in results:
        print("createtime:%s" % res[0].strftime('%H:%M'))
        createtime.append(res[0].strftime('%H:%M'))
        memory.append(res[1])
        cpu_load_5.append(res[2])
        disk.append(res[3])
        memory_spare.append(res[4])
        disk_spare.append(res[5])
        cpu_load_10.append(res[6])
        cpu_load_15.append(res[7])
    del results





    return render_to_response('dist/dashboard.html',
                              dict(username=request.session['username'].title(), displayDashboard=display_dashboard,
                                   createtime=createtime, memory=memory, cpu_load_5=cpu_load_5, disk=disk,
                                   memory_spare=memory_spare, disk_spare=disk_spare, usercount=len(session),
                                   cpu_load_10=cpu_load_10, cpu_load_15=cpu_load_15,is_main=1,menulist=menulist,submenulist=submenulist))


@login_required
@csrf_protect
def adduser(request):
    username = None
    page_range=None
    request.session.set_expiry(0)
    # print("session:" % dir(request.session))
    print("session:%s" % request.session.keys())

    if request.method == 'POST':
        form = UserSearch(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            request.session['search']=username

    else:
        form = UserSearch()


    if username is not None:
        userlist = User.objects.filter(~Q(username='admin'), username__contains=username)
    elif 'search_username' in request.GET:
        search_username=request.GET.get('search_username')
        userlist=User.objects.filter(~Q(username='admin'), username__contains=search_username).order_by(id)
    else:
        userlist = User.objects.exclude(username='admin')
    print("userlist:%s" % userlist)
    paginator = Paginator(userlist, 3)
    if 'page' in request.GET:
        page = int(request.GET.get('page'))
        display = 'block'
    else:
        page = 1
        display = 'block'
    if 'search_username' in request.GET:
        search_username=request.GET.get('search_username')

    print("display:%s page:%s" % (display, page))
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


#对于超过10页的按顺序依次显示
    if paginator.num_pages > 10:
        if page > 6:
             page_range=range(page-5,page+5)
        else:
            page_range=range(1,11)
    else:
        page_range=range(1,paginator.num_pages)

    return render(request, 'dist/users.html',
                  dict(username=request.session['username'].title(), userlist=users, userform=form, displayAdduser=display,
                       page_user=page,mainmenu=u'用户管理',submenu=u'添加用户',search_username=request.session.get('search'),menulist=menulist,submenulist=submenulist,page_range=page_range))


@login_required
@csrf_protect
def add_role(request):
    rolename = None
    request.session.set_expiry(0)
    print("session:%s" % dir(request.session['username']))
    if request.method == 'POST':
        form = RoleSearch(request.POST)
        if form.is_valid():
            rolename = form.cleaned_data['rolename']
    else:
        form = RoleSearch()


    if rolename is not None:
        rolelist = Group.objects.filter(name__contains=rolename).order_by(id)
    else:
        rolelist = Group.objects.order_by('id')
    paginator_role = Paginator(rolelist, 3)
    if 'page_role' in request.GET:
        page_role = request.GET.get('page_role')
        display_role = 'block'
    else:
        page_role = 1
        display_role = 'block'

    try:
        roles = paginator_role.page(page_role)
    except PageNotAnInteger:
        roles = paginator_role.page(1)
    except EmptyPage:
        roles = paginator_role.page(paginator_role.num_pages)

    userlist = User.objects.filter(~Q(username='admin'))
    print("userlist:%s" % userlist)

    print("display_role:%s" % display_role)
    return render(request, 'dist/roles.html',
                  dict(username=request.session['username'].title(), rolelist=roles, displayAddrole=display_role,
                       page_role=page_role, mainmenu=u'角色管理', submenu=u'添加角色', roleform=form,menulist=menulist,submenulist=submenulist,page_number=range(1,paginator_role.num_pages),allusers=userlist))


@login_required
@csrf_protect
def dropuser(request):
    username = None
    if request.method == 'POST':
        form = UserSearch(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
    else:
        form = UserSearch()
    if username is not None:
        userlist = User.objects.filter(~Q(username='admin'), username__contains=username).order_by(id)
    else:
        userlist = User.objects.exclude(username='admin')
    pagintor = Paginator(userlist, 3)
    if 'page' in request.GET:
        page = request.GET.get('page')
        display = 'block'
    else:
        page = 1
        display = 'block'

    print("display:%s page:%s" % (display, page))
    try:
        users = pagintor.page(page)
    except PageNotAnInteger:
        users = pagintor.page(1)
    except EmptyPage:
        users = paginator.page(pagintor.num_pages)

    return render(request, 'dist/users.html', {'username': request.session['username'].title(), 'userlist': users,
                                               'displayDeluser': display, 'mainmenu': u'用户管理', 'submenu':u'删除用户',
                                               'page_user': page, 'form': form,'menulist':menulist,'submenulist':submenulist})


@login_required
@csrf_protect
def deluser(request):
    if request.method == 'POST':
        userlist = request.POST.get('userlist')
        try:
            for userid in userlist.split(','):
                user = User.objects.get(id=userid)
                user.delete()
                print("aaaa ")
            # 1:success
            result = {'result': 1}
        except Exception as e:
            # 0:failure
            result = {'result': 0, 'message': str(e)}

        return HttpResponse(json.dumps(result), content_type='application/json')


@login_required
@csrf_protect
def addrole(request):
    if request.method == 'POST':
        rolename = request.POST.get('rolename')
        try:
            role = Group.objects.create(name=rolename)
            role.save()
            # 1:success
            result = {'result': 1}
        except Exception:
            # 0:failure
            result = {'result': 0}
        return HttpResponse(json.dumps(result), content_type='application/json')


@login_required
@csrf_exempt
def roleinfo(request):
    rolelist = Group.objects.all()
    paginator_role = Paginator(rolelist, 3, 2)
    page_role = request.GET.get('page_role')
    try:
        roles = paginator_role.page(page_role)
    except PageNotAnInteger:
        roles = paginator_role.page(1)
    except EmptyPage:
        roles = paginator_role.page(paginator_role.num_pages)
    return HttpResponse(json.dumps(roles), content_type='application/json')


@login_required
@csrf_exempt
def dropRole(request):
    rolename = None

    if request.method == 'POST':
        form = RoleSearch(request.POST)
        if form.is_valid():
            rolename = form.cleaned_data['rolename']
        if 'rolelist' in request.POST:
            rolelist = request.POST.get('rolelist')
            try:
                for roleid in rolelist.split(','):
                    role = Group.objects.get(id=roleid)
                    role.delete()
                result = {'result': 1}
            except Exception as e:
                print("has an error:%s" % e)
                result = {'result': 0}
            return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        form = RoleSearch()

    if rolename is not None:
        rolelist = Group.objects.filter(name__contains=rolename)
    else:
        rolelist = Group.objects.all().order_by('id')
    pagintor = Paginator(rolelist, 3)
    if 'page_role' in request.GET:
        page_role = request.GET.get('page_role')
        display_role = 'block1'
    else:
        page_role = 1
        display_role = 'block'

    print("display:%s page:%s" % (display_role, page_role))
    try:
        roles = pagintor.page(page_role)
    except PageNotAnInteger:
        roles = pagintor.page(1)
    except EmptyPage:
        roles = paginator.page(pagintor.num_pages)

    return render(request, 'dist/roles.html', {'username': request.session['username'].title(), 'rolelist': roles,
                                               'displayDelrole': display_role, 'page_role': page_role,
                                               'mainmenu': u'角色管理', 'submenu': u'删除角色', 'form': form,'menulist':menulist,'submenulist':submenulist})


@login_required
@csrf_exempt
def assign(request):
    rolename = ''
    userlist = []
    result = {}
    if request.method == 'POST':
        if 'userlist' in request.POST:
            userlist = request.POST.get('userlist')
        if 'rolename' in request.POST:
            rolename = request.POST.get('rolename')

        role = Group.objects.get(name=rolename)
        try:
            for user in regexp.split(userlist.rstrip()):
                print("username:%s" % user)
                selectuser = User.objects.get(username=user)
                selectuser.groups.add(role)
                result = {'result': 1}
        except Exception as e:
            result = {'result': 0, 'message': str(e)}
        return HttpResponse(json.dumps(result), content_type='application/json')


@login_required
@csrf_exempt
def removeassign(request):
    if request.method == 'POST':
        rolename = request.POST.get('rolename')
        container_users = request.POST.get('container_users')
        try:
            print("container_users:%s length:%d" % (container_users, len(container_users)))
            role = Group.objects.get(name=rolename)
            if len(container_users.split(",")) == 0:
                role.user_set.clear()
                print("n " * 10)
            else:
                print("y " * 10)
                container_users = container_users.split(",")
                # print("type of container_users:%s" % type(container_users))
                userlist = User.objects.exclude(username__in=container_users)
                for user in userlist:
                    print("User:%s" % user)
                    user = User.objects.get(username=user)
                    role.user_set.remove(user)
            result = {'result': 1}
        except Exception as e:
            result = {'result': 0, 'message': str(e)}

        return HttpResponse(json.dumps(result), content_type='application/json')


class Login(View):
    def get(self, req):
        print('req method:%s list:%s' % (req.method, dir(req)))
        return HttpResponse('')


def addmenu(request):
    if request.method=='POST':
        form=MenuForm(request.POST)
        if form.is_valid():
            menuname=form.cleaned_data['menuname']
            url=form.cleaned_data['url']
    else:
        form=MenuForm()

    return render(request, 'dist/menu.html', dict(displayMenu='block', mainmenu=u'菜单管理', submenu=u'添加菜单',form=form,menulist=menulist,submenulist=submenulist))


def readfile(filename,chunksize=1024):
    with open(filename) as f:
        while True:
            c=f.read(chunksize)
            if c:
                yield c
            else:
                break

def download(request):
    filename=request.GET.get('filename')
    response=StreamingHttpResponse(readfile(filename))
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachement;filename={}'.format(filename.split('/')[-1])
    print("StreamingHttpResponse:%s" % dir(response))
    return response
