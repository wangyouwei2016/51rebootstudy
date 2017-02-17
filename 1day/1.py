#coding=utf-8
import MySQLdb
conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='weiwei',
                db='yp',
                charset='utf8',
            )
cur = conn.cursor()
f = open("/home/wangyw/yp.txt", "r")
while True:
    line = f.readline()
    if line:
        #处理每行\n
        line = line.strip('\n')
        line = line.split(":")
        print (line)
        # if line in 'uuid':
        #     print (line)
        # uuid = line[1]
        # print uuid




#         province = line[1]
#         city = line[2]
#         call_type = line[3]
#         cur.execute(
#             "insert into data9(tel,province,city,cell_type) values(%s,%s,%s,%s)",
#             [tel, province, city, call_type])
    else:
        break
# f.close()
# cur.close()
# conn.commit()
# conn.close()