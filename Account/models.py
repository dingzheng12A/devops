from django.db import models

# Create your models here.
class Coststatistics(models.Model):
    id = models.AutoField(primary_key=True)
    ProductCode = models.CharField(verbose_name="产品编号",max_length=10)
    SubscriptionType = models.CharField(verbose_name="计费类型",max_length=30)
    PaymentAmount = models.FloatField(verbose_name="费用",default=0.0)
    BillingCycle = models.DateField(verbose_name="账单期")

