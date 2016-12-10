#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: IcySun
# 脚本功能：分析apache日志 统计高频IP 和高频url

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import Counter
import os

logname = '/home/wangyw/access_log.log'
ipcount = []
urlcount = []
for x in open(logname).readlines():
    ip = x.split(' ')[0]
    url = x.split(' ')[8]
    ipcount.append(ip)
    urlcount.append(url)
iplist = Counter(ipcount)
urllist = Counter(urlcount)
print '======正在分析的日志======'
for ip,count1 in iplist.most_common(5):
    print '[+] 访问IP: %s ,访问次数: %d' % (ip,count1)

for url,count2 in urllist.most_common(15):
    print '[+] 访问URL: %s ,访问次数: %d' % (url,count2)