from django.contrib import admin

# Register your models here.
from django import forms
from django.db.models import Max
from ckeditor.widgets import CKEditorWidget

from monitor.models import Monitor, Post, Blog
from monitor.models import Post, Blog

def get_title(modeladmin, request, queryset):
    memory_used = map(lambda x: str(x.memory_used), queryset)
    for item in memory_used:
        print(item)
    return "".join(memory_used)


get_title.short_description = "获取所有标题"


def copy_instance(modeladmin, request, queryset):
    for item in queryset:
        temp = item
        max_id = Monitor.objects.all().aggregate(Max('id'))
        print("max_id:%(max_id)s" % {"max_id": max_id})
        temp.id = int(max_id.get("id__max", 0)) + 1
        print("id:{id}".format(id=temp.id))
        temp.save()


copy_instance.short_description = "复制所选对象"

class MonitorAdmin(admin.ModelAdmin):
    list_display = ["memory_used", "cpu_used", "disk_used"]
    list_editable = ('cpu_used',)
    list_display_links = ()
    search_fields = ("memory_used",)
    date_hierarchy = "createTime"
    list_filter = ["cpu_used", "memory_used"]
    filter_horizontal = ('host',)
    actions = [get_title, copy_instance]


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "body"]


admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
