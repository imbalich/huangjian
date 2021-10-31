from apps.IHSD.customDef.matrixDef import matrix_pg as pg
from apps.IHSD.customDef.matrixDef import matrix_zy as yc
import numpy as np
import pymysql
#数据库连接



def get_conn(dbwm,password):
    conn =  pymysql.connect(host='127.0.0.1', user='root', passwd=password, db=dbwm, charset='utf8')
    return conn

#关闭连接

def close_conn(conn,cursor):
    cursor.close()
    conn.close()

#检测数据查询
def jcsj_cx(table,dbwm,password):
    db = get_conn(dbwm,password)
    cursor = db.cursor()
    # query = "select * from {0} order by id desc limit 50;".format(table)
    query = "select * from {0} order by id ;".format(table)
    cursor.execute(query)
    record_50 = cursor.fetchall()
    close_conn(db, cursor)
    return record_50
#检测值评价结果(温度，挠度，应变)
def pjjg(table,dengji_1,dengji_2,dengji_3,dengji_4,dbwm,password):
    jg=[]
    for weizhi in range(1,6):
    # weizhi=1                       # 传感器位置
        shuju=np.array(jcsj_cx(table,dbwm,password))
        cx=shuju[:,weizhi]
        listLen=len(cx)
        a,b,c,d,e=0,0,0,0,0
        for i in cx:
            if float(i)<=dengji_1:
                a=a+1
            else:
                if float(i)<=dengji_2:
                    b=b+1
                else:
                    if float(i)<=dengji_3:
                        c=c+1
                    else:
                        if float(i)<=dengji_4:
                            d=d+1
                        else:
                            e=e+1
        #单个传感器的结果
        jg_dg=[a,b,c,d,e]
        for i in range(5):
            jg_dg[i]=jg_dg[i]/listLen
        # 整体结果
        jg.append(jg_dg)
    jg=np.array(jg)
    return  jg

#锈蚀
def pjjg_xiushi(table,dengji_1,dengji_2,dengji_3,dengji_4,dbwm,password):
    jg=[]
    for weizhi in range(1,6):
    # weizhi=1                       # 传感器位置
        shuju=np.array(jcsj_cx(table,dbwm,password))
        cx=shuju[:,weizhi]
        listLen=len(cx)
        a,b,c,d,e=0,0,0,0,0
        for i in cx:
            if float(i)>=dengji_1:
                a=a+1
            else:
                if float(i)>=dengji_2:
                    b=b+1
                else:
                    if float(i)>=dengji_3:
                        c=c+1
                    else:
                        if float(i)>=dengji_4:
                            d=d+1
                        else:
                            e=e+1
        #单个传感器的结果
        jg_dg=[a,b,c,d,e]
        for i in range(5):
            jg_dg[i]=jg_dg[i]/listLen
        # 整体结果
        jg.append(jg_dg)
    jg=np.array(jg)
    return  jg

# 模糊评价（温度、挠度，应变）
def mhpj(table,weight, dengji_1, dengji_2, dengji_3, dengji_4,dbwm,password):
    jg = pjjg(table, dengji_1, dengji_2, dengji_3, dengji_4,dbwm,password)
    mhpj = np.matmul(weight,jg)
    return mhpj
#锈蚀
def mhpj_xiushi(table,weight, dengji_1, dengji_2, dengji_3, dengji_4,dbwm,password):
    jg = pjjg_xiushi(table, dengji_1, dengji_2, dengji_3, dengji_4,dbwm,password)
    mhpj = np.matmul(weight,jg)
    return mhpj
def dengjipinggu(dbwm,password):
    #各类型模糊评价
    #温度
    table='ihsd_t_wendu'                # 查看的类型
    dengji_1=150
    dengji_2=250
    dengji_3=400
    dengji_4=500
    weight=pg.weight_wendu
    jieguo_wd=mhpj(table,weight, dengji_1, dengji_2, dengji_3, dengji_4,dbwm,password)
    #应变
    table='ihsd_t_yingbian'                # 查看的类型
    dengji_1=2000
    dengji_2=4000
    dengji_3=6000
    dengji_4=8000
    weight=pg.weight_yingbian
    jieguo_yb=mhpj(table,weight, dengji_1, dengji_2, dengji_3, dengji_4,dbwm,password)
    #挠度
    table='ihsd_t_naodu'                # 查看的类型
    dengji_1=1
    dengji_2=3
    dengji_3=6
    dengji_4=30
    weight=pg.weight_naodu
    jieguo_nd=mhpj(table,weight, dengji_1, dengji_2, dengji_3, dengji_4,dbwm,password)
    #锈蚀
    table='ihsd_t_xiushi'                # 查看的类型
    dengji_1=-50
    dengji_2=-125
    dengji_3=-175
    dengji_4=-225
    weight=pg.weight_xiushi
    jieguo_xs=mhpj_xiushi(table,weight, dengji_1, dengji_2, dengji_3, dengji_4,dbwm,password)

    #模糊关系矩阵
    mhgx_R=np.array([jieguo_xs,jieguo_nd,jieguo_yb,jieguo_wd])

    # 综合评价
    zhpj=np.matmul(pg.weight_lx,mhgx_R)
    #等级值
    dengjijuzheng=np.array([[100],[95],[80],[60],[40]])
    djz=np.matmul(zhpj,dengjijuzheng)[0]
    #等级值判断
    dj=0
    if djz>95.00:
        dj=1
    else:
        if djz>80.00:
            dj=2
        else:
            if djz>60.00:
                dj=3
            else:
                if djz>40.00:
                    dj=4
                else:
                    dj=5
    return dj
def ztms(dj):
    ztms = {
        0:"暂无数据。",
        1:"状态良好，钢桥主要部位的结构件状态优良",
        2:"钢桥主要部位状态正常，部分承重出现细微损坏，有锈蚀现象，局部出现裂缝。",
        3:"钢桥可以正常使用，但主要结构件损坏较大，裂缝宽度已经超出理论值。",
        4:"钢桥主要结构件破坏范围较为严重，护栏、面板等表面涂漆出现剥落并有大面积锈蚀现象，"
          "在车辆承载下会出现功能性病害，维持最初钢桥运营水平较为困难。",
        5:"钢桥主要结构件严重破坏或截面损失，桥梁整体病害严重。承载能力远远小于设计标准，"
          "无法满足正常交通要求，特殊情况下需要关闭桥梁运行。"
    }
    return ztms.get(dj, None)

#计算矩阵
def juzheng(juzheng,z,y,year):
    zs=z
    if zs<=4:
        while zs!=0 :
            zs=zs-1
            juzheng[zs]=8
        juzheng[z]=y
    else:
        for i in range(4):
            juzheng[i]=8
        juzheng[4]=year-32
    return juzheng

#未来状态预测及描述
def yuce(year,yearYuce,dbwm,password):
    # 当前桥梁状态向量
    i = dengjipinggu(dbwm,password) - 1
    ztxl = [0, 0, 0, 0, 0]
    ztxl[i] = 1
    ztxl = np.mat(ztxl)
    # 桥梁已服役时长（年）
    work_year = year
    work_year = int(work_year)
    work_year_z = work_year // 8
    work_year_y = work_year % 8
    yuce_year = yearYuce
    yuce_year = int(yuce_year)
    yuce_year = yuce_year + work_year
    yuce_year_z = yuce_year // 8
    yuce_year_y = yuce_year % 8
    gongzuozhuangtai = [0, 0, 0, 0, 0]
    yuce = [0, 0, 0, 0, 0]
    gongzuozhuangtai = np.mat([juzheng(gongzuozhuangtai, work_year_z, work_year_y, work_year)])
    yuce = np.mat([juzheng(yuce, yuce_year_z, yuce_year_y, yuce_year)])
    yuce = yuce - gongzuozhuangtai
    a, b, c, d, e = int(yuce[0, 0]), int(yuce[0, 1]), int(yuce[0, 2]), int(yuce[0, 3]), int(yuce[0, 4])  # 指数
    # 预测状态等级
    ztxl = ztxl * (yc.stage_1 ** a) * (yc.stage_2 ** b) * (yc.stage_3 ** c) * (yc.stage_4 ** d) * (yc.stage_5 ** e)
    yuce_dengji = ztxl * yc.yc_dengji
    rank_yuce = float(yuce_dengji[0, 0])
    if rank_yuce < (i+1):
        rank_yuce=i+1
    rank=str(rank_yuce)
    miaoshu_xuhao = rank_yuce // 1
    if miaoshu_xuhao < 1:
        miaoshu_xuhao = 1
    miaoshu_yuce = ztms(miaoshu_xuhao)
    resultList=[rank_yuce,miaoshu_yuce,miaoshu_xuhao]

    return resultList

