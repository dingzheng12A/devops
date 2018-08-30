from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Hosts(models.Model):
        id=models.IntegerField(primary_key=True,default=1)
        hostname=models.CharField(max_length=256,default='')
        ipaddr=models.CharField(max_length=256)
        sshport=models.IntegerField(default=22)
        remote_user=models.CharField(max_length=40)
        host_desc=models.CharField(max_length=256)
 
        class Meta:
        	app_label = 'Hosts'
        	ordering = ['name']


class Host(models.Model):
    id = models.CharField(max_length=100, primary_key=True, verbose_name="实例名称")
    region = models.CharField(max_length=20, verbose_name="数据中心", default="")
    az = models.CharField(max_length=20, verbose_name="可用区", default="")
    mem = models.IntegerField(verbose_name="内存", default=0)
    cpu = models.IntegerField(verbose_name="CPU", default=0)
    status = models.CharField(max_length=10, verbose_name="状态", default="")
    created = models.DateTimeField(verbose_name="创建时间", auto_now=True)
    expire = models.DateTimeField(verbose_name="过期时间", auto_now=True)
    instance_type = models.CharField(max_length=20, verbose_name="实例类型", default="")
    instance_name = models.CharField(max_length=50, verbose_name="实例名称", default="")
    hostname = models.CharField(max_length=50, verbose_name="主机名", default="")
    internet_ip = models.GenericIPAddressField(verbose_name="公网IP", default="0.0.0.0")
    internet_charge = models.CharField(max_length=100, verbose_name="流量支付模式", default="")
    internal_ip = models.GenericIPAddressField(verbose_name="内网IP", default="0.0.0.0")
    elastic_ip = models.GenericIPAddressField(verbose_name="弹性IP", default="0.0.0.0")
    charge_type = models.CharField(max_length=20, verbose_name="支付方式", default="")
    desc = models.CharField(max_length=100, verbose_name="备注", default="")
    os_type = models.CharField(max_length=30, verbose_name="操作系统类型")
    tags = models.CharField(max_length=100, verbose_name="实例标签")

    def __str__(self):
        return self.instance_name


class Metric(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    cpu_avg = models.IntegerField(verbose_name="cpu平均值", validators=[MinValueValidator(0), MaxValueValidator(100)])
    cpu_max = models.IntegerField(verbose_name="cpu峰值", validators=[MinValueValidator(0), MaxValueValidator(100)])
    mem_avg = models.IntegerField(verbose_name="mem平均值", validators=[MinValueValidator(0), MaxValueValidator(100)])
    mem_max = models.IntegerField(verbose_name="mem峰值", validators=[MinValueValidator(0), MaxValueValidator(100)])
    iops_avg = models.IntegerField(verbose_name="iops平均值", validators=[MinValueValidator(0), MaxValueValidator(100)])
    iops_max = models.IntegerField(verbose_name="iosp峰值", validators=[MinValueValidator(0), MaxValueValidator(100)])
    writeiops_avg = models.IntegerField(verbose_name="写操作iops平均值", validators=[MinValueValidator(0), MaxValueValidator(100)],default=0)
    writeiops_max = models.IntegerField(verbose_name="写操作iops峰值", validators=[MinValueValidator(0), MaxValueValidator(100)],default=0)
    network_avg = models.IntegerField(verbose_name="网卡流量平均值", validators=[MinValueValidator(0), MaxValueValidator(100)])
    network_max = models.IntegerField(verbose_name="网卡流量峰值", validators=[MinValueValidator(0), MaxValueValidator(100)])
    load_avg = models.IntegerField(verbose_name="系统负载均值", validators=[MinValueValidator(0), MaxValueValidator(100)])
    load_max = models.IntegerField(verbose_name="系统负载峰值", validators=[MinValueValidator(0), MaxValueValidator(100)])
    created = models.DateTimeField(verbose_name="生成时间", auto_now=True)
