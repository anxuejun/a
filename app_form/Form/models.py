#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile_Name(models.Model):
    username = models.OneToOneField(User)
    postation = models.CharField(max_length=64)
    def __unicode__(self):
        return self.username


class Group(models.Model):
    cable_ip = models.CharField(max_length=128,unique=True,blank=True,null=True)
    wireless_ip = models.CharField(max_length=128,unique=True,blank=True,null=True)
    def __unicode__(self):
        return self.cable_ip+self.wireless_ip



class Asset(models.Model):
    asset_type_choices = (
        (0,"台式机"),
        (1,"笔记本"),
        (2,"苹果一体机"),
        (3,"显示器"),
        (4,"自带笔记本"),
        (5,"服务器")
    )
    asset_username = models.CharField(max_length=30,default='xebest')
    asset_postation = models.CharField(max_length=128,blank=True,null=True)
    asset_cable_ip = models.CharField(max_length=128,blank=True,null=True)
#    asset_wireless_ip = models.CharField(max_length=128,blank=True,null=True)
    asset_type = models.SmallIntegerField(choices=asset_type_choices)
    asset_num = models.CharField(max_length=64,blank=True,null=True)
    asset_configuration = models.CharField(max_length=64,blank=True,null=True)
    asset_remarks = models.TextField(blank=True,null=True)
    def __unicode__(self):
        return self.get_asset_type_display()

class Shines(models.Model):
    shines_notes =  models.CharField(max_length=128,verbose_name='备注')
    shines_neiwang_ip = models.CharField(max_length=128,blank=True,null=True,verbose_name='内网ip')
    shines_waiwang_ip = models.CharField(max_length=128,blank=True,null=True,verbose_name='外网ip')
    def __unicode__(self):
        return self.shines_notes
