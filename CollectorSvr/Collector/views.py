from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import random
import json
import OpenOPC

# Create your views here.
def tank4C9(request):
    assert isinstance(request,HttpRequest)
    return render(
        request,'Collector/tank4C9.html',)

def getCollectorData(request):
    tank4C9 = {
            'DeviceID':1,
            'DeviceName':'1#反应罐',
            'Status' : 0,#设备运行状态
            'OverheadFlow':0,#顶流量
            'ButtomsFlow':0,#低流量
            'Power':0,#功率
        }
    opc = OpenOPC.client()
    opc.connect('OPCJ.SampleServer.1')
    tank4C9['OverheadFlow'] = opc['Random.Int1']
    tank4C9['ButtomsFlow'] = opc['Random.Int2']
    tank4C9['Power'] = opc['Random.Int3']
    opc.close()
    Collector={
        'CollectorId':1,
        'CollectorName':'1#采集器',
        'Status':0,
        'DeviceList':[tank4C9],
        }
    return HttpResponse( json.dumps(Collector) )

def getTank4C9Data(request):
    tank4C9 = {
            'Status' : random.randint(0,1),#设备运行状态
            'OverheadFlow':random.randint(1,10),#顶流量
            'ButtomsFlow':random.randint(1,10),#低流量
            'Power':random.randint(10000,100000),#功率
        }

    return HttpResponse( json.dumps(tank4C9) )