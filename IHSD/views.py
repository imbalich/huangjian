from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


from tools.paging import PageInfo2
import IHSD.models as models
from apps.IHSD.customDef.gradeEstimation import dengjipinggu,ztms,yuce
from apps.IHSD.customDef.db import dataRecord
# Create your views here.

#数据库名称
dbwm='bimsb'
#数据库密码
password='123456'


wdSensorType = ''
wdSensorLocation = ''
wdQuantity =  None
def wdInfo(request):
    global wdSensorType
    global wdSensorLocation
    global wdQuantity
    wdSensorType = request.GET.get('sensorType')
    wdSensorLocation = request.GET.get('sensorLocation')
    if request.GET.get('quantity') =='':
        wdQuantity = None
    else:
        wdQuantity = int(request.GET.get('quantity'))
    return render(request, 'ihsd/ihsd_warningData.html', locals())

def to_warningData_inquire(request):
    print(wdQuantity)
    if wdSensorType =="1":
        if wdSensorLocation == "0":
            yujing_list = models.t_yujing_wd.objects.filter()[:wdQuantity]
        else:
            yujing_list = models.t_yujing_wd.objects.filter(y_name=wdSensorLocation)[:wdQuantity]
    elif wdSensorType =="2":
        if wdSensorLocation == "0":
            yujing_list = models.t_yujing_yb.objects.filter()[:wdQuantity]
        else:
            yujing_list = models.t_yujing_yb.objects.filter(y_name=wdSensorLocation)[:wdQuantity]
    elif wdSensorType =="3":
        if wdSensorLocation == "0":
            yujing_list = models.t_yujing_xs.objects.filter()[:wdQuantity]
        else:
            yujing_list = models.t_yujing_xs.objects.filter(y_name=wdSensorLocation)[:wdQuantity]
    else :
        if wdSensorLocation == "0":
            yujing_list = models.t_yujing_nd.objects.filter()[:wdQuantity]
        else:
            yujing_list = models.t_yujing_nd.objects.filter(y_name=wdSensorLocation)[:wdQuantity]
    base_url = '/ihsd/warningDataInquire/?'+'sensorType='+wdSensorType+'&sensorLocation='+wdSensorLocation+\
               '&quantity='+str(wdQuantity)
    page_info = PageInfo2(request.GET.get('page'),10,yujing_list.count(),5, base_url)
    user_list_final = yujing_list[page_info.start():page_info.end()]
    return render(request, 'ihsd/ihsd_warningData.html',locals())
#页面跳转
# def to_warningData(request):
#     return render(request, 'IHSD/ihsd_warningData.html',locals())
#健康状态查询
def to_healthStatusGrade(request):
    try:
        dj=dengjipinggu(dbwm,password)#评估健康等级
    except:
        dj=0
    info=ztms(dj)#评估结果描述
    return render(request, 'IHSD/ihsd_healthStatusGrade.html',locals())
#跳转到监控页面
def to_dataMonitor(request):
    return render(request, 'IHSD/ihsd_dataMonitor.html',locals())
#实时查看信息AJAX
def to_dataChang(request):
    sensorType = request.GET.get('sensorType')
    sensorLocation = request.GET.get('sensorLocation')
    #打开数据库插入数据并对传入数据进行实时判断 将超过预警值的数据同时加入到预警数据库中
    #目前采用的是随机生成数据并插入数据库中，若连接硬件数据采集系统时需要将下面的“dataRecord（）”函数放入开辟的新线程中
    dataRecord(dbwm,password)
    #搜索数据库信息
    if sensorType == "wendu":
        sensorList = models.t_wendu.objects.filter().values().order_by('-id').first()
    elif sensorType == "yingbian":
        sensorList = models.t_yingbian.objects.filter().values().order_by('-id').first()
    elif sensorType == "xiushi":
        sensorList = models.t_xiushi.objects.filter().values().order_by('-id').first()
    else:
        sensorList = models.t_naodu.objects.filter().values().order_by('-id').first()
    time = sensorList['y_time']
    data = sensorList[sensorType+'_'+sensorLocation]
    print(time)
    print(data)
    resultDict = {'time':time,'data':data}
    return JsonResponse(resultDict)
#未来健康等级查询AJAX
def mytext(request):
    year=request.GET.get('year')
    yearYuce = request.GET.get('yearYuce')
    try:
        resultList=yuce(year,yearYuce,dbwm,password)
        dj='%.2f' % resultList[0]
        xuhao=resultList[2]
    except:
        dj = 0
        xuhao=0
    info=ztms(xuhao)
    resultDict={"dj":dj,"info":info}
    print(resultDict)
    return JsonResponse(resultDict)

# def to_test(request):
#     return render(request, 'IHSD/test.html', locals())



