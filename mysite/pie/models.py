from django.db import models
from django.conf import settings
# Create your models here.


# class City(models.Model):
#     country = models.CharField(max_length=30)
#     population = models.IntegerField(null=True, blank=True)
#

class DjangoBoard(models.Model):

    srcip = models.GenericIPAddressField()
    srcport = models.IntegerField(null=True, blank=True)
    dstip = models.GenericIPAddressField()
    dstport = models.IntegerField(null=True, blank=True)
    protocol = models.CharField(max_length=30)
    flowduration = models.BigIntegerField(null=True, blank=True)
    flowpackets_s = models.FloatField(null=True, blank=True)
    label = models.IntegerField(null=True, blank=True)

class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    userid = models.CharField(max_length=20)
    userpw = models.CharField(max_length=20)

