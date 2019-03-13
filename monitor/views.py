from django.shortcuts import render
from django.http import HttpResponse
from monitor.forms import PostAdminForm

# Create your views here.
def get_filename(filename):
    return filename.upper()

def aaa(request):
    if request.method == "POST":
        forms = PostAdminForm()
    else:
        forms = PostAdminForm()
    return render(request, template_name="../backup/aaa.html", context=locals())


def xxx(request):
    if request.method == "GET":
        res = request.GET.get("content")
        print("res:%(content)s" % {"content": res})
    return HttpResponse("")
