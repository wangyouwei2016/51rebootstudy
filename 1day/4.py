#encoding:utf -8
#fromkeys 快速从list转化为一个dict
#dict.keys() 获取字典中的key的list
#dict.value()获取字典中的value的list
#dict.items()获取字典中每个元素的list
#popitem从dict里随机弹出值

#作业
#一个log ，按照ip和访问状态两个维度统计数据，打印前十名，并且以html表格的形式展示


#1.读取www_access文件，ip和code作为dict的key，遍历出每个key出现次数，生成dict
f = open('/home/wangyw/www_access_20140823.log','r')
http_dict = {}
done = 0
for line in f.readlines():
    if  line.split():
        ip =  line.split()[0]
        code =  line.split()[8]
        key = (ip,code)
        http_dict[key] = http_dict.setdefault(key,0) +1
f.close()
#2.生成index.html文件，将html文件的开头写入文件
f = open('index.html','w')
f.write('<table border="1"><tr><td>ip</td><td>code</td><td>count</td></tr>')
f.close()

#3.追加方式打开index.html文件，遍历dict ，排序，并将写入index.html
f = open('index.html','a+')
#3.1 反转dict生成新的dict 排序，取出前十
stat_dict ={}
stat_list = []
for key in http_dict:
    stat_dict[http_dict[key]] = key
    stat_list.append(http_dict[key])
for i in range(len(stat_list)-1):
    for j in range(len(stat_list)-1-i):
        if stat_list[j] > stat_list[j+1]:
            stat_list[j],stat_list[j+1] = stat_list[j+1],stat_list[j]
stat_list = stat_list[-1:-11:-1]
#3.2 以key为索引，遍历新生成的dict，这样key为出现的次数，value为(ip,code)，所以stat_dict[key][0]为ip，stat_dict[key][1]为code
for key in stat_list:
    f.write('<tr><td> %s</td><td>%s</td> <td>%s</td></tr> \n' %(stat_dict[key][0],stat_dict[key][1],key))
f.write(' </table>')
f.close()
