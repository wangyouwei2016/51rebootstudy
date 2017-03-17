# coding=utf-8
import MySQLdb

f = open("/home/wangyw/yp.txt" , "r")
line = f.readlines()
UUID = []
NAME = []
POWST = []
for i in line:
    if i[0:4] in "uuid":
        i = i.strip('\n').split(':')[1]
        UUID.append(i)

    if i[5:9] in "name" and len(i) != 1:
        i = i.strip('\n').split(':')[1]
        NAME.append(i)

    if i[4:9] in "power" and len(i) != 1:
        i = i.strip('\n').split(':')[1]
        POWST.append(i)

T = zip(UUID , NAME , POWST)
for data in T:
    # print data

    # 连接mysql的方法：connect(host='localhost',user='root',passwd='root',db='test',port=3306)
    con = MySQLdb.connect(
        host='localhost' ,
        port=3306 ,
        user='root' ,
        passwd='weiwei' ,
        db='yp' ,
        charset='utf8' ,
    )
    # 所有的查询，都在连接con的一个模块cursor上面运行的
    cur = con.cursor()

    sql = "insert into ypaclome (uuid,name,powst) values (%s,%s,%s)"

    params = (data[0] , data[1] , data[2])
    print params
    temp = cur.execute(sql , params)
    con.commit()
    con.close()
    # sql = "insert into table(key1,key2,key3) values (%s,%s,%s)"%(value1,value2,value3)
    # 执行一个查询
    # cur.execute("SELECT VERSION()")
    # 取得上个查询的结果，是单个结果
    # data = cur.fetchone()
    # print "Database version : %s " % data

    # print mm
    # print UUID
    # print NAME
    # print POWST



    #     IP = i.split()[0]
    #     STAT = i.split()[8]
    #     Sdict.setdefault(IP + ":" + STAT , 0)
    #     Sdict[IP + ":" + STAT] += 1
    # Sdata.close()

    # lines = f.readlines()
    # dic = {}
    # for line in lines:
    #     if line.split():
    #         if line.split()[0] not in dic:
    #             dic[line.split()[0]] = {}
    #             dic[line.split()[0]][line.split()[8]] = 1
    #         elif line.split()[8] not in dic[line.split()[0]]:
    #             dic[line.split()[0]][line.split()[8]] = 1
    #         else:
    #             dic[line.split()[0]][line.split()[8]] = dic[line.split()[0]][line.split()[8]] + 1
    # f.close()
    # print dic

    # while True:
    #     line = f.readline()
    #     if len(line)!=1:
    #         #处理每行\n
    #         line = line.strip('\n')
    #         line = line.split(":")
    #         print len(line)
    #         # if line in 'uuid':
    #         #     print (line)
    #         # uuid = line[1]
    #         # print uuid
    #
    #
    #
    #
    # #         province = line[1]
    # #         city = line[2]
    # #         call_type = line[3]
    # #         cur.execute(
    # #             "insert into data9(tel,province,city,cell_type) values(%s,%s,%s,%s)",
    # #             [tel, province, city, call_type])
    #     else:
    #         break
    # # f.close()
    # # cur.close()
    # # conn.commit()
    # # conn.close()
