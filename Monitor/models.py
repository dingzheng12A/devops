from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Monitor(models.Model):
	id=models.AutoField(primary_key=True)
	memory_used=models.FloatField(verbose_name="内存MB",default=0)
	memory_spare=models.FloatField(verbose_name="剩余内存MB",default=0)
	cpu_load_5m=models.FloatField(verbose_name="统计当前平均5分钟负载",default=0)
	cpu_load_10m=models.FloatField(verbose_name="统计当前平均10分钟负载",default=0)
	cpu_load_15m=models.FloatField(verbose_name="统计当前平均15分钟负载",default=0)
	disk_used=models.FloatField(verbose_name="统计磁盘使用情况",default=0)
	disk_spare=models.FloatField(verbose_name="剩余硬盘MB",default=0)
	createtime = models.DateTimeField(verbose_name="生成时间", auto_now=True)

	class Meta:
		db_table='resource_monitor'
		permissions=(
			("open_monitor","can open monitor to query"),
			("reply_monitor","can reply monitor"),
			("close_monitor","close monitor"),
		)