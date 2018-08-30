from django.db import models
import datetime
import django.utils.timezone as timezone
# Create your models here.
class Menu(models.Model):
        id=models.AutoField(primary_key=True)
        name=models.CharField(max_length=64,null=False,verbose_name=u'Menu name')
        parent_id=models.IntegerField(default=0,verbose_name=u'Parent menu id')
        url=models.CharField(max_length=128,verbose_name=u'link url address')
        create_time=models.DateTimeField(default=timezone.now,verbose_name=u'create time')
         
        class Meta:
                db_table='sys_menu'
