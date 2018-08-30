from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from  django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import  ContentType

# Create your views here.
class Mylogin(View):
    def get(self,request):
        print("request method:%s" % request.method )
        username=request.GET.get('username')
        password=request.GET.get('password')
        return HttpResponse("request method:%s username:%s password:%s" % (request.method,username,password))

    @csrf_exempt
    def post(self,request):
        print("request method:%s" % request.method)
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse("request method:%s username:%s password:%s" % (request.method, username, password))

if __name__=='__main__':
    content_type=ContentType.objects.get(app_label='Monitor',model='Monitor')
    permission=Permission.objects.create(codename='play_book',name='can play book',content_type=content_type)


