from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from ckeditor.fields import  RichTextField, RichTextFormField
# Create your models here.





class Post(models.Model):
	content = RichTextField()

class Blog(models.Model):
	title = models.CharField(max_length=200, unique=True)
	body = RichTextField()
	body1 = RichTextFormField()


	def __str__(self):
		return self.title


class Monitor(models.Model):
	choices = (
		("", "------"),
		("title1", "标题1"),
		("title2", "标题2"),
		("title3", "标题3")
	)
	id = models.AutoField(primary_key=True)
	memory_used = models.FloatField(verbose_name="内存MB", default=0)
	cpu_used = models.FloatField(verbose_name="统计当前cpu使用率", default=0)
	disk_used = models.FloatField(verbose_name="统计磁盘使用情况", default=0)
	createTime = models.DateTimeField(verbose_name="生成时间", auto_now=True)
	host = models.ManyToManyField(Blog, verbose_name="标题", blank=True)
	lists = models.CharField(choices=choices, max_length=50,default="------")

	class Meta:
		db_table = 'resource_monitor'
		verbose_name = "系统资源监控"



