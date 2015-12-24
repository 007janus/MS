from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from hostinfo.models import Host
from hostinfo.models import Server

def index(req):
    print req
    if req.method == 'POST':
        hostname = req.POST.get('hostname')
        ip = req.POST.get('ip')
        osversion = req.POST.get('osversion')
        memory = req.POST.get('memory')
        disk = req.POST.get('disk')
        vendor_id = req.POST.get('vendor_id')
        model_name = req.POST.get('model_name')
        cpu_core = req.POST.get('cpu_core')
        product = req.POST.get('product')
        Manufacturer = req.POST.get('Manufacturer')
        sn = req.POST.get('sn')
        desc = req.POST.get('desc')
        memorysize = req.POST.get('memorysize')
        disksize = req.POST.get('disksize')
        cpu = req.POST.get('cpu')
        house = req.POST.get('house')
        houseid = req.POST.get('houseid')
        Unum = req.POST.get('Unum')
        Uid = req.POST.get('Uid')
        try:
            host = Host.objects.get(hostname=hostname)
        except:
            host = Host()

        host.hostname = hostname
        host.ip = ip
        host.osversion = osversion
        host.memory = memory
        host.disk = disk
        host.vendor_id = vendor_id
        host.model_name = model_name
        host.cpu_core = cpu_core
        host.product = product
        host.Manufacturer = Manufacturer
        host.sn = sn
        host.save()

        return HttpResponse('ok')
    else:
        return HttpResponse('no data')

def index1(req):
    print req
    if req.method == 'POST':
        ip = req.POST.get('ip')
        vip = req.POST.get('vip')
        outip = req.POST.get('outip')
        service = req.POST.get('service')
        desc = req.POST.get('desc')
        rd = req.POST.get('rd')
        try:
            host = Host.objects.get(hostname=hostname)
        except:
            host = Host()

        host.outip = outip
        host.ip = ip
        host.vip = vip
        host.service = service
        host.desc = desc
        host.rd = rd
        host.save()

        return HttpResponse('ok')
    else:
        return HttpResponse('no data')

