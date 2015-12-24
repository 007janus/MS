import xadmin
from hostinfo.models import Host
from hostinfo.models import Server
from hostinfo.models import MysqlAccount
from hostinfo.models import OtherAccount
from hostinfo.models import ServerAccount
from hostinfo.models import IPinfo

class HostAdmin(object):
    list_display = [
	    'hostname',
		'ip',
		'osversion',
		'memory',
		'disk',
		'vendor_id',
		'model_name',
		'cpu_core',
	    'product',
		'Manufacturer',
		'sn',
		'desc',
		'memorysize',
		'disksize',
		'cpu',
		'house',
		'houseid',
		'Unum',
		'Uid']
    search_fields = ('hostname','ip','osversion','memory','disk','vendor_id','model_name','cpu_core','product','Manufacturer','sn','desc','memorysize','disksize','cpu','house','houseid','Unum','Uid')

class ServerAdmin(object):
    list_display = [
	    'vip',
		'ip',
		'outip',
		'service',
		'desc',
		'rd']
    search_fields = ('vip','ip','outip','service','desc','rd')

class IPinfoAdmin(object):
    list_display = [
	    'vip',
		'ip',
		'outip',
		'farip',
		'desc']
    search_fields = ('vip','ip','outip','farip','desc')

class ServerAccountAdmin(object):
    list_display = [
	    'osaccount',
		'ip',
		'pas',
		'farip',
		'faraccount',
		'farpas',
		'desc']
    search_fields = ('vip','ip','outip','farip','desc','faraccount','farpas')

class MysqlAccountAdmin(object):
    list_display = [
	    'sql',
		'ip',
		'pas',
		'sqlaccount',
		'authority',
		'rang',
		'desc']
    search_fields = ('sql','ip','pas','sqlaccount','authority','rang','desc')

class OtherAccountAdmin(object):
    list_display = [
	    'name',
		'ip',
		'url',
		'account',
		'authority',
		'pas',
		'desc']
    search_fields = ('name','ip','pas','account','authority','url','desc')
xadmin.site.register(Host,HostAdmin)
xadmin.site.register(OtherAccount,OtherAccountAdmin)
xadmin.site.register(MysqlAccount,MysqlAccountAdmin)
xadmin.site.register(ServerAccount,ServerAccountAdmin)
xadmin.site.register(IPinfo,IPinfoAdmin)
xadmin.site.register(Server,ServerAdmin)

