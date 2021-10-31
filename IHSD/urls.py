from django.urls import path
from . import views

urlpatterns = [
    #预警信息页面
    path('warningDataInquire/', views.to_warningData_inquire, name='warningDataInquire'),
    # path('warningData/', views.to_warningData, name='warningData'),
    path('wdInfo/', views.wdInfo, name='wdInfo'),

    #健康状态查询页面
    path('healthStatusGrade/', views.to_healthStatusGrade, name='healthStatusGrade'),
    path('mytext/', views.mytext, name='mytext'),

    #实时监控页面
    path('dataMonitor/', views.to_dataMonitor, name='dataMonitor'),
    path('dataChange/', views.to_dataChang, name='dataChang'),
    # path('test/', views.to_test, name='test'),

]