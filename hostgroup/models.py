from django.db import models

# Create your models here.
class HostGroup(models.Model):
        __tablename__="sys_hostgroup"
        id=models.IntegerField(primary_key=True)
        group_name=models.CharField(max_length=256)
        group_desc=models.CharField(max_length=256)
        def __repr__(self):
                return '<HostGroup {}>'.format(self.id)
