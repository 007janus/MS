import xadmin
from hostinfo.models import Host

class HostAdmin(object):
#class HostAdmin(object):
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
		'sn']

xadmin.site.register(Host,HostAdmin)

