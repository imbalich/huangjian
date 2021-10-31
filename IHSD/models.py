from django.db import models

# Create your models here.

class t_naodu(models.Model):
    '''
    桥梁各节点的挠度数据
    '''
    naodu_1 = models.CharField(max_length=64,verbose_name='1号测量点挠度值', null=True, blank=True)
    naodu_2 = models.CharField(max_length=64, verbose_name='2号测量点挠度值', null=True, blank=True)
    naodu_3 = models.CharField(max_length=64, verbose_name='3号测量点挠度值', null=True, blank=True)
    naodu_4 = models.CharField(max_length=64, verbose_name='4号测量点挠度值', null=True, blank=True)
    naodu_5 = models.CharField(max_length=64, verbose_name='5号测量点挠度值', null=True, blank=True)
    y_time = models.CharField(max_length=64, verbose_name='挠度记录时间', null=True, blank=True)

class t_wendu(models.Model):
    '''
    桥梁各节点的温度数据
    '''
    wendu_1 = models.CharField(max_length=64,verbose_name='1号测量点温度值', null=True, blank=True)
    wendu_2 = models.CharField(max_length=64, verbose_name='2号测量点温度值', null=True, blank=True)
    wendu_3 = models.CharField(max_length=64, verbose_name='3号测量点温度值', null=True, blank=True)
    wendu_4 = models.CharField(max_length=64, verbose_name='4号测量点温度值', null=True, blank=True)
    wendu_5 = models.CharField(max_length=64, verbose_name='5号测量点温度值', null=True, blank=True)
    y_time = models.CharField(max_length=64, verbose_name='温度记录时间', null=True, blank=True)

class t_xiushi(models.Model):
    '''
    桥梁各节点的锈蚀数据
    '''
    xiushi_1 = models.CharField(max_length=64,verbose_name='1号测量点锈蚀值', null=True, blank=True)
    xiushi_2 = models.CharField(max_length=64, verbose_name='2号测量点锈蚀值', null=True, blank=True)
    xiushi_3 = models.CharField(max_length=64, verbose_name='3号测量点锈蚀值', null=True, blank=True)
    xiushi_4 = models.CharField(max_length=64, verbose_name='4号测量点锈蚀值', null=True, blank=True)
    xiushi_5 = models.CharField(max_length=64, verbose_name='5号测量点锈蚀值', null=True, blank=True)
    y_time = models.CharField(max_length=64, verbose_name='锈蚀记录时间', null=True, blank=True)

class t_yingbian(models.Model):
    '''
    桥梁各节点的应变数据
    '''
    yingbian_1 = models.CharField(max_length=64,verbose_name='1号测量点应变值', null=True, blank=True)
    yingbian_2 = models.CharField(max_length=64, verbose_name='2号测量点应变值', null=True, blank=True)
    yingbian_3 = models.CharField(max_length=64, verbose_name='3号测量点应变值', null=True, blank=True)
    yingbian_4 = models.CharField(max_length=64, verbose_name='4号测量点应变值', null=True, blank=True)
    yingbian_5 = models.CharField(max_length=64, verbose_name='5号测量点应变值', null=True, blank=True)
    y_time = models.CharField(max_length=64, verbose_name='应变记录时间', null=True, blank=True)

class t_yujing_nd(models.Model):
    '''
    桥梁挠度超警记录
    其中包括超警数值来源|数值大小|记录时间
    '''
    y_name = models.CharField(max_length=64,verbose_name='挠度超警位置', null=True, blank=True)
    y_shuzhi = models.CharField(max_length=64,verbose_name='挠度超警数值', null=True, blank=True)
    y_time = models.CharField(max_length=64, verbose_name='挠度超警记录时间', null=True, blank=True)

class t_yujing_wd(models.Model):
    '''
    桥梁温度超警记录
    其中包括超警数值来源|数值大小|记录时间
    '''
    y_name = models.CharField(max_length=64,verbose_name='温度超警位置', null=True, blank=True)
    y_shuzhi = models.CharField(max_length=64,verbose_name='温度超警数值', null=True, blank=True)
    y_time = models.CharField(max_length=64, verbose_name='温度超警记录时间', null=True, blank=True)

class t_yujing_xs(models.Model):
    '''
    桥梁锈蚀超警记录
    其中包括超警数值来源|数值大小|记录时间
    '''
    y_name = models.CharField(max_length=64,verbose_name='锈蚀超警位置', null=True, blank=True)
    y_shuzhi = models.CharField(max_length=64,verbose_name='锈蚀超警数值', null=True, blank=True)
    y_time = models.CharField(max_length=64, verbose_name='锈蚀超警记录时间', null=True, blank=True)

class t_yujing_yb(models.Model):
    '''
    桥梁应变超警记录
    其中包括超警数值来源|数值大小|记录时间
    '''
    y_name = models.CharField(max_length=64,verbose_name='应变超警位置', null=True, blank=True)
    y_shuzhi = models.CharField(max_length=64,verbose_name='应变超警数值', null=True, blank=True)
    y_time = models.CharField(max_length=64, verbose_name='应变超警记录时间', null=True, blank=True)