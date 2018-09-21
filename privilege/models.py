from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Privilege(models.Model):
    id=models.AutoField(primary_key=True,default=1,max_length=11)
    pid=models.IntegerField(validators=[MinValueValidator(10)])
    privilege_name=models.CharField(max_length=200)
    request_method=models.CharField(max_length=10)
    request_url=models.CharField(max_length=300)

    class Meta:
        db_table='sys_privilege'
