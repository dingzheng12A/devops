from django.db import models
from django.contrib.auth.models import User
import os
import hashlib
import Devops.settings as settings
from django.contrib.auth.models import Group
from django.contrib.auth.models import  Permission,GroupManager


# Create your models here.


def upload_to(instance, filename):
    suffix = filename.split(".")[-1]
    img_path = os.path.join(settings.UPLOAD_PATH, instance.username, hashlib.md5(
        (instance.username + "_" + filename).encode("utf-8")).hexdigest() + "." + suffix).replace("\\", "/")
    print("path:", settings.UPLOAD_PATH)
    return img_path


class MediaList(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(verbose_name="用户名", max_length=50)
    img_path = models.ImageField(upload_to=upload_to, default=None)
    img_url = models.CharField(max_length=200, verbose_name="url 路径")
    user = User.objects.get(username='admin')

    class Meta:
        db_table = "media_list"

class MyGroup(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, primary_key=True)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = "groups"

# class RoleManager(models.Manager):
#     def get_query_set(self):
#         return super(RoleManager, self).get_query_set().filter(student__enrolled=True).distinct()
#
# class MyGroup(models.Model):
#     group_id = models.AutoField(primary_key=True,auto_created=True,default=1)
#     description = models.CharField(max_length=200, default="")
#     group_name = models.CharField(('name'), max_length=80, unique=True, default="")
#     permission_list = models.ManyToManyField(
#         Permission,
#         verbose_name=('permissions'),
#         blank=True,
#     )
#
#     objects = RoleManager()
#
#     class Meta:
#         db_table = "groups"
#         verbose_name = ('group')
#         verbose_name_plural = ('groups')
#
#     def __str__(self):
#         return self.name

    # def natural_key(self):
    #     return (self.name,)



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)