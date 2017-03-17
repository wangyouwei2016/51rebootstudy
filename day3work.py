#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from collections import Counter
import os

logname = '/home/wangyw/www_access_20140823.log'
ipcount = []
stcount = []
for x in open(logname).readlines():
    if x.split():
        ip = x.split()[0]
        st = x.split()[8]
        ipcount.append(ip)
        stcount.append(st)
iplist = Counter(ipcount)
stlist = Counter(stcount)
print '======正在分析的日志======'
for ip,count1 in iplist.most_common(10):
    print '[+] 访问IP: %s ,访问次数: %d' % (ip,count1)

for st,count2 in stlist.most_common(10):

    print '[+] 访问状态: %s ,出现次数: %d' % (st,count2)
# # top1ip = iplist.most_common(5)[0][0]
# # url = "http://freeapi.ipip.net/{}".format(top1ip)
# # req = urllib2.Request(url)
# # res_data = urllib2.urlopen(req)
# # res = res_data.read().decode('utf-8')
# # # csres = res_data.read().decode('utf-8')[2:4]
# #
# # if iplist.most_common(5)[0][0]not in liwaiip:
# #     print iplist.most_common(5)[0][0]
# #     print res
# #     print urllist.most_common(5)[0][0]
