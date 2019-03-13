from django.db import models
from datetime import datetime

# Create your models here.
choice = (
    ('success', 1),
    ('failure', 0)
)


class Buildhistory(models.Model):
    id = models.AutoField(primary_key=True)
    jobname = models.CharField(max_length=50, verbose_name=u"job 名称")
    buildid = models.IntegerField(verbose_name="Build Id", default="")
    viewname = models.CharField(max_length=50, verbose_name=u"试图名称")
    parameters = models.CharField(max_length=200, verbose_name=u"构建参数", default="")
    starttime = models.DateTimeField(verbose_name=u"开始构建时间", default=datetime.now)
    buildtime = models.FloatField(max_length=20, verbose_name=u"构建时间", default=0)
    buildresult = models.CharField(choices=choice, verbose_name=u"构建结果", max_length=20)

    class Meta:
        db_table = "Buildhistory"
