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
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.sessions.models import Session
from main.forms import UserCreateForm
from main.forms import GroupCreateForm
from main.models import  MyGroup

from django.http import StreamingHttpResponse
from Devops.settings import DATABASES
from Devops import settings
from Devops import settings
import hashlib
import os
import logging

logger = logging.getLogger(__name__)
collect_logger = logging.getLogger('collect')

from main.forms import UserModifyForm
from menu.menuQuery import menulist, submenulist
from privilege.models import Privilege
from main.models import MediaList

regexp = re.compile('\s+')


# Create your views here.

@csrf_protect
def login(request):
    get_token(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_active:
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


@csrf_exempt
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
            result = {'result': 0, 'message': 'failure for adduser!'}

        return HttpResponse(json.dumps(result), content_type='application/json')


@login_required
def batch_delete_user(request):
    if request.method == "POST":
        user_list = request.POST.get("user_list").lstrip(",")
        print("user_list:", user_list)
        try:
            for uid in user_list.split(","):
                print("uid:{uid}".format(uid=uid))
                user = User.objects.get(id=int(uid))
                user.delete()
            result = {"result": 1}
        except BaseException as e:
            print("has an error:%s" % str(e))
            result = {"result": 0}
    return HttpResponse(json.dumps(result), content_type="application/json")


def monitor_resource(sql):
    database = DATABASES.get('default', None)
    conn = pymysql.connect(host=database.get("HOST"), port=int(database.get("PORT")), user=database.get("USER"),
                           password=database.get("PASSWORD"), charset='utf8', db=database.get('NAME'))
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


@csrf_protect
@login_required
def mainpage(request):
    request.session.set_expiry(0)
    username = request.session['username']
    logger.info("user:{username} already login".format(username=username))
    now = datetime.datetime.now()
    display_dashboard = 'block'
    before_20_minute = datetime.timedelta(minutes=-20)
    first_time = (now + before_20_minute)
    session = Session.objects.all()
    sql = r"SELECT createtime,memory_used,cpu_load_5m,disk_used,memory_spare,disk_spare,cpu_load_10m,cpu_load_15m " \
          r"FROM resource_monitor WHERE CREATETIME>'%s'" % first_time.strftime('%Y-%m-%d %H:%M')

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
        createtime.append(res[0].strftime('%H:%M'))
        memory.append(res[1])
        cpu_load_5.append(res[2])
        disk.append(res[3])
        memory_spare.append(res[4])
        disk_spare.append(res[5])
        cpu_load_10.append(res[6])
        cpu_load_15.append(res[7])
    del results

    img_path, user_modify_form = common(request, username=username)
    print("img_url:", "/static/" + img_path)
    return render(request, 'dist/dashboard.html', dict(
        username=request.session['username'].title(), img_url="/static/" + img_path,
        displayDashboard=display_dashboard,
        createtime=createtime, memory=memory, cpu_load_5=cpu_load_5, disk=disk,
        memory_spare=memory_spare, disk_spare=disk_spare, usercount=len(session),
        cpu_load_10=cpu_load_10, cpu_load_15=cpu_load_15, is_main=1, menulist=menulist,
        submenulist=submenulist, user_modify_form=user_modify_form))


PAGE_SIZE = 5
PAGE = 1


@login_required
@csrf_protect
def user_manager(request):
    global PAGE_SIZE, PAGE
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.create()
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()
        if 'pagesize' in request.POST:
            PAGE_SIZE = int(request.POST.get("pagesize"))
    else:
        form = UserCreateForm()

    if request.method == "GET":
        if 'page' in request.GET:
            PAGE = int(request.GET.get("page"))
    user_list = User.objects.filter()
    page_size = PAGE_SIZE
    current_page = PAGE
    func_1 = lambda x, y: (divmod(x, y)[0], divmod(x, y)[0])
    pages, last_records = func_1(len(user_list), page_size)
    if current_page < pages:
        current_user_list = user_list[(current_page - 1) * page_size:current_page * page_size]
    else:
        current_user_list = user_list[(current_page - 1) * page_size:]
    print("last_records:", last_records)
    if last_records != 0:
        pages += 1
    print("pages:", pages)
    if pages > 10:
        if current_page > 6 and current_page + 5 < pages:
            page_list = list(range(current_page - 5, current_page + 5))
        elif current_page + 5 >= pages:
            page_list = list(range(pages - 10, pages))
        else:
            page_list = list(range(1, 11))
    else:
        page_list = list(range(1, pages+1))
    username = request.session['username']
    img_url = "/static/" + str(MediaList.objects.filter(username=username)[0].img_url) if len(
        MediaList.objects.filter(username=username)) > 0 else ""
    username = request.session['username'].title()
    img_path, user_modify_form = common(request, username=username)
    menu_info = {}
    menu_info["mainmenu"] = "用户和组"
    menu_info["submenu"] = "用户管理"
    menu_info["sub_url"] = "/user/usermanager"
    return render(request, template_name="dist/users.html", context=locals())


@login_required
def is_user_exists(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        user = User.objects.filter(username=username)
        if user:
            result = {"result": 0, "message": "用户已经存在"}
            return HttpResponse(json.dumps(result), content_type="application/json")
        user_email = User.objects.filter(email=email)
        if user_email:
            result = {"result": 0, "message": "邮箱地址已经使用"}
            return HttpResponse(json.dumps(result), content_type="application/json")
        result = {"result": 1}
    else:
        result = {"result": 0}
    return HttpResponse(json.dumps(result), content_type="application/json")


@login_required
def upload_image(request):
    print("test " * 10)
    try:
        username = request.session.get("username")

        if request.method == "POST":
            media = MediaList.objects.filter(username=username)
            filename = request.FILES.get("FileUpload").name
            suffix = filename.split(".")[-1]
            if not len(media):
                media = MediaList.objects.create()
                media.username = username
                media.img_path = request.FILES.get("FileUpload")
                media.img_url = os.path.join(settings.UPLOAD_PATH, username, hashlib.md5(
                    (username + "_" + filename).encode("utf-8")).hexdigest() + "." + suffix)
                media.save()
            else:
                media[0].img_path = request.FILES.get("FileUpload")
                media[0].img_url = os.path.join(settings.UPLOAD_PATH, username, hashlib.md5(
                    (username + "_" + filename).encode("utf-8")).hexdigest() + "." + suffix).split("/", 2)[-1].replace(
                    "\\", "/")
                print(dir(request.FILES.get("FileUpload")))
                print("fileupload:", request.FILES.get("FileUpload"))
                media[0].save()
            result = {"result": 1}
    except BaseException as e:
        logging.error("上传图片错误:{error}".format(error=str(e)))
        result = {"result": 0}
    return HttpResponse(json.dumps(result), content_type="application/json")


@csrf_protect
@login_required
def modify_user(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            result = {"result": 1}
        except BaseException:
            result = {"result": 0}
        return HttpResponse(json.dumps(result), content_type="application/json")
    else:
        return


# @login_required
# @csrf_protect
# def add_role(request):
#     rolename = None
#     request.session.set_expiry(0)
#     print("session:%s" % dir(request.session['username']))
#     if request.method == 'POST':
#         form = RoleSearch(request.POST)
#         if form.is_valid():
#             rolename = form.cleaned_data['rolename']
#     else:
#         form = RoleSearch()
#
#     if rolename is not None:
#         rolelist = Group.objects.filter(name__contains=rolename).order_by(id)
#     else:
#         rolelist = Group.objects.order_by('id')
#     paginator_role = Paginator(rolelist, 3)
#     if 'page_role' in request.GET:
#         page_role = request.GET.get('page_role')
#         display_role = 'block'
#     else:
#         page_role = 1
#         display_role = 'block'
#
#     try:
#         roles = paginator_role.page(page_role)
#     except PageNotAnInteger:
#         roles = paginator_role.page(1)
#     except EmptyPage:
#         roles = paginator_role.page(paginator_role.num_pages)
#
#     userlist = User.objects.filter(~Q(username='admin'))
#     print("userlist:%s" % userlist)
#     privilist = Privilege.objects.filter(pid=0)
#     subprivlist = Privilege.objects.filter(~Q(pid=0))
#
#     print("display_role:%s" % display_role)
#     return render(request, 'dist/roles.html',
#                   dict(username=request.session['username'].title(), rolelist=roles, displayAddrole=display_role,
#                        page_role=page_role, mainmenu=u'角色管理', submenu=u'添加角色', roleform=form, menulist=menulist,
#                        submenulist=submenulist, page_number=range(1, paginator_role.num_pages), allusers=userlist,
#                        privilist=privilist, subprivlist=subprivlist))


def common(request, username=""):
    if request.method == "POST":
        user_modify_form = UserModifyForm(request.POST)
        if user_modify_form.is_valid():
            username = user_modify_form.cleaned_data.get("username")
            password = user_modify_form.cleaned_data.get("password")
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
    else:
        user_modify_form = UserModifyForm()
    img_path = str(MediaList.objects.filter(username=username)[0].img_url).replace("'", "") if len(
        MediaList.objects.filter(username=username)) > 0 else ""
    return img_path, user_modify_form


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
            result = {'result': 1}
        except Exception:
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


# @login_required
# @csrf_exempt
# def dropRole(request):
#     rolename = None
#
#     if request.method == 'POST':
#         form = RoleSearch(request.POST)
#         if form.is_valid():
#             rolename = form.cleaned_data['rolename']
#         if 'rolelist' in request.POST:
#             rolelist = request.POST.get('rolelist')
#             try:
#                 for roleid in rolelist.split(','):
#                     role = Group.objects.get(id=roleid)
#                     role.delete()
#                 result = {'result': 1}
#             except Exception as e:
#                 print("has an error:%s" % e)
#                 result = {'result': 0}
#             return HttpResponse(json.dumps(result), content_type='application/json')
#     else:
#         form = RoleSearch()
#
#     if rolename is not None:
#         rolelist = Group.objects.filter(name__contains=rolename)
#     else:
#         rolelist = Group.objects.all().order_by('id')
#     pagintor = Paginator(rolelist, 3)
#     if 'page_role' in request.GET:
#         page_role = request.GET.get('page_role')
#         display_role = 'block1'
#     else:
#         page_role = 1
#         display_role = 'block'
#
#     print("display:%s page:%s" % (display_role, page_role))
#     try:
#         roles = pagintor.page(page_role)
#     except PageNotAnInteger:
#         roles = pagintor.page(1)
#     except EmptyPage:
#         roles = paginator.page(pagintor.num_pages)
#
#     return render(request, 'dist/roles.html', {'username': request.session['username'].title(), 'rolelist': roles,
#                                                'displayDelrole': display_role, 'page_role': page_role,
#                                                'mainmenu': u'角色管理', 'submenu': u'删除角色', 'form': form,
#                                                'menulist': menulist, 'submenulist': submenulist})


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


# def addmenu(request):
#     if request.method == 'POST':
#         form = MenuForm(request.POST)
#         if form.is_valid():
#             menuname = form.cleaned_data['menuname']
#             url = form.cleaned_data['url']
#     else:
#         form = MenuForm()
#
#     return render(request, 'dist/menu.html',
#                   dict(displayMenu='block', mainmenu=u'菜单管理', submenu=u'添加菜单', form=form, menulist=menulist,
#                        submenulist=submenulist))
#
#
# def readfile(filename, chunksize=1024):
#     with open(filename) as f:
#         while True:
#             c = f.read(chunksize)
#             if c:
#                 yield c
#             else:
#                 break
#
#
# def download(request):
#     filename = request.GET.get('filename')
#     response = StreamingHttpResponse(readfile(filename))
#     response['Content-Type'] = 'application/octet-stream'
#     response['Content-Disposition'] = 'attachement;filename={}'.format(filename.split('/')[-1])
#     print("StreamingHttpResponse:%s" % dir(response))
#     return response
#
#
# def addprivileged(request):
#     return render(request, 'dist/privilege.html', dict(menulist=menulist, submenulist=submenulist))
#
#
# def download1(request):
#     response = HttpResponse(content_type='application/csv')
#     response['Content-Disposition'] = 'attachment; filename="loss_customer.csv"'
#     writer = csv.writer(response)
#     writer.writerow(["用户名", "屏数量", "卡数量", "邮箱", "电话", "最后登陆时间"])
#     return response
#
#
# @csrf_exempt
# def test1(request):
#     user = ""
#     password = ""
#     if 'user' in request.POST:
#         user = request.POST.get('user')
#     if 'password' in request.POST:
#         password = request.POST.get('password')
#     return HttpResponse(json.dumps({"user": user, "password": password}), content_type="application/json")
#
#
# def vue(request):
#     return render(request, 'dist/vue_test.html')

from main.tasks import add


def produce(a, b):
    try:
        r = add.delay(a, b)
    except Exception as e:
        print(str(e))
        return False
    return True


@login_required
def group_manager(request):
    global GROUP_PAGE_SIZE, GROUP_PAGE
    GROUP_PAGE_SIZE = 5
    GROUP_PAGE = 1
    if request.method == "POST":
        group_form = GroupCreateForm(request.POST)
        if group_form.is_valid():
            group = Group.objects.create(name=group_form.clean()['groupname'])
            group.save()
            mygroup = MyGroup.objects.create(group=group,description=group_form.cleaned_data["description"])
            mygroup.save()
    else:
        group_form = GroupCreateForm()
    menu_info = {}
    menu_info["mainmenu"] = "用户和组"
    menu_info["submenu"] = "组管理"
    menu_info["sub_url"] = "/user/groupmanager"
    if request.method == "GET":
        if 'page' in request.GET:
            PAGE = int(request.GET.get("page"))
    group_list = MyGroup.objects.filter()
    page_size = GROUP_PAGE_SIZE
    current_page = GROUP_PAGE
    func_1 = lambda x, y: (divmod(x, y)[0] + 1, divmod(x, y)[0])
    pages, last_records = func_1(len(group_list), page_size)
    if current_page < pages:
        current_group_list = group_list[(current_page - 1) * page_size:current_page * page_size]
    else:
        current_group_list = group_list[(current_page - 1) * page_size:]
    if last_records != 0:
        pages += 1
    if pages > 10:
        if current_page > 6 and current_page + 5 < pages:
            page_list = list(range(current_page - 5, current_page + 5))
        elif current_page + 5 >= pages:
            page_list = list(range(pages - 10, pages))
        else:
            page_list = list(range(1, 11))
    else:
        page_list = list(range(1, pages))
    user_list = User.objects.filter()
    return render(request, template_name="dist/groups.html", context=locals())


@login_required
def is_group_exists(request):
    if request.method == "POST":
        group_name = request.POST.get("group_name")
        group = MyGroup.objects.filter(group=group_name)
        if group:
            result = {"result": 0, "message": "组已经存在"}
            return HttpResponse(json.dumps(result), content_type="application/json")
        result = {"result": 1}
    else:
        result = {"result": 0}
    return HttpResponse(json.dumps(result), content_type="application/json")


@login_required
def assign_to(request):
    if request.method == 'POST':
        user_list = request.POST.get("user_list")
        group_id = request.POST.get("group_id")
        print("userlist:{user_list}".format(user_list=user_list))
        if user_list:
            user_list = user_list.split(",")
            for user in user_list:
                # print("username:{user}".format(user=user))
                user = User.objects.get(username=user)
                group = MyGroup.objects.get(group_id=group_id)
                user.groups.add(group.group)
        else:
            pass
    return HttpResponse(json.dumps({"result":1}),content_type="application/json")


@login_required
def query_users(request):
    if request.method == "POST":
        group_id = request.POST.get("group_id")
        """获取当前角色组"""
        group = MyGroup.objects.get(group_id=group_id)
        user_list = []
        """查询当前组关联的用户"""
        for user_record in group.group.user_set.values():
            user = {}
            user['id'] = user_record.get('id')
            user['username'] = user_record.get('username')
            user_list.append(user)

        result = {"result":1,"user_list":user_list}
    else:
        result = {"result":0}
    return HttpResponse(json.dumps(result), content_type="application/json")

