from django.contrib import admin

# Register your models here.
from django.contrib import admin
from main.models import MediaList
# from main.models import  MyGroup


class MediaListAdmin(admin.ModelAdmin):
    list_display = ("img_url",)
    # list_editable = ("username",)
    # filter_horizontal = ("username",)


class MyGroupAdmin(admin.ModelAdmin):
    list_display = ("group","description")
    # filter_horizontal = ("permission_list",)


admin.site.register(MediaList, MediaListAdmin)
# admin.site.register(MyGroup, MyGroupAdmin)