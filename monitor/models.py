from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Monitor(models.Model):
	id=models.AutoField(primary_key=True,auto_add=True)
	memory_used=models.FloatField(verbose_name="内存MB",default=0)
	cpu_used=models.FloatField(verbose_name="统计当前cpu使用率",default=0)
	disk_used=models.FloatField(verbose_name="统计磁盘使用情况",default=0)
	createtime = models.DateTimeField(verbose_name="生成时间", auto_now=True)

	class Meta:
        	db_table='resource_monitor'
