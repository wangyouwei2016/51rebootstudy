#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: IcySun
# 脚本功能：分析apache日志 统计高频IP 和高频url
import urllib2,urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import Counter
import os
liwaiip = ['59.46.22.351','59.46.22.352']
logname = '/home/wangyw/access_log.log'
ipcount = []
urlcount = []
for x in open(logname).readlines():
    ip = x.split(' ')[0]
    url = x.split(' ')[7]
    ipcount.append(ip)
    urlcount.append(url)
iplist = Counter(ipcount)
urllist = Counter(urlcount)
# print '======正在分析的日志======'
# for ip,count1 in iplist.most_common(5):
#     print '[+] 访问IP: %s ,访问次数: %d' % (ip,count1)
#
# for url,count2 in urllist.most_common(15):
#     print '[+] 访问URL: %s ,访问次数: %d' % (url,count2)
top1ip = iplist.most_common(5)[0][0]
url = "http://freeapi.ipip.net/{}".format(top1ip)
req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = res_data.read().decode('utf-8')
# csres = res_data.read().decode('utf-8')[2:4]
if iplist.most_common(5)[0][0]not in liwaiip:
    print iplist.most_common(5)[0][0]
    print res