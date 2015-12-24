#coding:utf8
from django.db import models

# Create your models here.
class Host(models.Model):
    hostname = models.CharField(u"主机名", max_length=50)
    ip = models.IPAddressField(u'IP')
    osversion = models.CharField(u'操作系统',max_length=50)
    memory = models.CharField(u'内存型号',max_length=50)
    memorysize = models.CharField(u'内存大小',max_length=50, default="null")
    disk = models.CharField(u'磁盘型号',max_length=50)
    disksize = models.CharField(u'磁盘大小',max_length=50, default="null")
    vendor_id = models.CharField(u'供应商ID',max_length=50)
    model_name = models.CharField(u'型号',max_length=50)
    cpu_core = models.CharField(u'CPU核数',max_length=50)
    cpu = models.CharField(u'CPU型号',max_length=50, default="null")
    product = models.CharField('服务器型号',max_length=50)
    Manufacturer = models.CharField(u'制造商',max_length=50)
    sn = models.CharField(max_length=50)
    house = models.CharField(u'机房',max_length=50, default="null")
    houseid = models.CharField('机柜',max_length=50, default="null")
    Unum = models.CharField(u'U数',max_length=50, default="null")
    Uid = models.CharField(u'U位',max_length=50, default="null")
    desc = models.CharField(u'备注',max_length=50, default="null")

    class Meta:
        verbose_name = "硬件信息"

class Server(models.Model):
    vip = models.IPAddressField(u'VIP')
    ip = models.IPAddressField(u'IP')
    outip = models.IPAddressField(u'外网IP')
    service = models.CharField(u'服务',max_length=50)
    rd = models.CharField(u'RD接口人',max_length=50)
    desc = models.CharField(u'备注',max_length=50)

    class Meta:
        verbose_name = "服务信息"

class IPinfo(models.Model):
    vip = models.IPAddressField(u'VIP')
    ip = models.IPAddressField(u'IP')
    outip = models.IPAddressField(u'外网IP')
    farip = models.IPAddressField(u'远程管理IP')
    desc = models.CharField(u'备注',max_length=50)

    class Meta:
        verbose_name = "IP信息"


class ServerAccount(models.Model):
    ip = models.IPAddressField(u'IP')
    osaccount = models.CharField(u'系统帐号',max_length=50)
    pas = models.CharField(u'系统密码',max_length=50)
    farip = models.CharField(u'远程管理卡IP',max_length=50)
    faraccount = models.CharField(u'管理卡帐号',max_length=50)
    farpas = models.CharField(u'管理卡密码',max_length=50)
    desc = models.CharField(u'备注',max_length=50)

    class Meta:
        verbose_name = "服务帐号信息"


class MysqlAccount(models.Model):
    ip = models.IPAddressField(u'IP')
    sql = models.CharField(u'数据库',max_length=50)
    sqlaccount = models.CharField(u'帐号',max_length=50)
    pas = models.CharField(u'密码',max_length=50)
    authority = models.CharField(u'权限',max_length=50)
    ran = models.CharField(u'访问范围',max_length=50)
    desc = models.CharField(u'备注',max_length=50)

    class Meta:
        verbose_name = "数据库帐号信息"


class OtherAccount(models.Model):
    name = models.CharField(u'名字',max_length=50)
    ip = models.IPAddressField(u'访问范围')
    url = models.CharField(u'地址',max_length=50)
    account = models.CharField(u'帐号',max_length=50)
    authority = models.CharField(u'权限',max_length=50)
    pas = models.CharField(u'密码',max_length=50)
    desc = models.CharField(u'备注',max_length=50)

    class Meta:
        verbose_name = "其他帐号信息"


