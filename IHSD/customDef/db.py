import pymysql
pymysql.install_as_MySQLdb()
import random
import time
def suijicharu(db_wm,table, weizhi_1, weizhi_2,weizhi_3,weizhi_4,weizhi_5,shuzhi_1,shuzhi_2,shuzhi_3,shuzhi_4,shuzhi_5,timeData,y_time,password):
    db = pymysql.connect(host='127.0.0.1', user='root', passwd=password, db=db_wm, charset='utf8')
    cursor = db.cursor()
    query = "insert into {10}({5},{6},{7},{8},{9},{11}) " \
            "value({0},{1},{2},{3},{4},'%s');".format(shuzhi_1,shuzhi_2,shuzhi_3,shuzhi_4,shuzhi_5,weizhi_1, weizhi_2,weizhi_3,weizhi_4,weizhi_5,table,y_time) % (timeData)
    cursor.execute(query)
    db.commit()

def mysql_crxx(db_wm, table, y_name, y_shuzhi, y_time,password):
    db = pymysql.connect(host='127.0.0.1', user='root', passwd=password, db=db_wm, charset='utf8')
    cursor = db.cursor()
    query = "insert into %s (y_name,y_shuzhi,y_time) values('%s','%s','%s')" % (table, y_name, y_shuzhi, y_time)
    cursor.execute(query)
    db.commit()


 # 数据库名
def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec
# 每一秒执行一次

def dataRecord(db_wm,password):
    # second = sleeptime(0, 0, 5)  放入新线程时请启动取消该行的注释
    # while switch == 1:   放入新线程时请启动取消该行的注释
        #db_wm：  服务器名字
        y_time='y_time'
        # time.sleep(second)
        timeData = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        #温度
        listWd=[]
        table='ihsd_t_wendu'
        tableYj='ihsd_t_yujing_wd'
        weizhi_1='wendu_1'
        weizhi_2='wendu_2'
        weizhi_3='wendu_3'
        weizhi_4='wendu_4'
        weizhi_5='wendu_5'
        for i in range(5):
            shuizhi=random.randint(0, 750)#随机生成数据
            listWd.append(shuizhi)
            if shuizhi > 700:               #预警值设置
                mysql_crxx(db_wm, tableYj, i+1, shuizhi, timeData,password)
        suijicharu(db_wm, table,weizhi_1, weizhi_2,weizhi_3,weizhi_4,weizhi_5,listWd[0],
                   listWd[1],listWd[2],listWd[3],listWd[4],timeData,y_time,password)
        #挠度
        listNd = []
        table = 'ihsd_t_naodu'
        tableYj = 'ihsd_t_yujing_nd'
        weizhi_1 = 'naodu_1'
        weizhi_2 = 'naodu_2'
        weizhi_3 = 'naodu_3'
        weizhi_4 = 'naodu_4'
        weizhi_5 = 'naodu_5'
        for i in range(5):
            shuizhi = round(random.uniform(0, 40),2)
            listNd.append(shuizhi)
            if shuizhi > 30:
                mysql_crxx(db_wm, tableYj, i+1, shuizhi, timeData,password)
        suijicharu(db_wm,table, weizhi_1, weizhi_2, weizhi_3, weizhi_4, weizhi_5,listNd[0],
                   listNd[1],listNd[2],listNd[3],listNd[4],timeData,y_time,password)
        # 应变
        listYb = []
        table = 'ihsd_t_yingbian'
        tableYj = 'ihsd_t_yujing_yb'
        weizhi_1 = 'yingbian_1'
        weizhi_2 = 'yingbian_2'
        weizhi_3 = 'yingbian_3'
        weizhi_4 = 'yingbian_4'
        weizhi_5 = 'yingbian_5'
        for i in range(5):
            shuizhi = random.randint(0,10000)
            listYb.append(shuizhi)
            if shuizhi > 8000:
                mysql_crxx(db_wm, tableYj, i+1, shuizhi, timeData,password)
        suijicharu(db_wm, table, weizhi_1, weizhi_2, weizhi_3, weizhi_4, weizhi_5,listYb[0],
                   listYb[1],listYb[2],listYb[3],listYb[4],timeData,y_time,password)
        # 锈蚀
        listXs = []
        table = 'ihsd_t_xiushi'
        tableYj = 'ihsd_t_yujing_xs'
        weizhi_1 = 'xiushi_1'
        weizhi_2 = 'xiushi_2'
        weizhi_3 = 'xiushi_3'
        weizhi_4 = 'xiushi_4'
        weizhi_5 = 'xiushi_5'
        for i in range(5):
            shuizhi = random.randint(-300, 0)
            listXs.append(shuizhi)
            if shuizhi < -225:
                mysql_crxx(db_wm, tableYj, i+1, shuizhi, timeData,password)
        suijicharu(db_wm, table, weizhi_1, weizhi_2, weizhi_3, weizhi_4, weizhi_5, listXs[0],
                   listXs[1],listXs[2],listXs[3],listXs[4],timeData,y_time,password)

        #预警数据插入
