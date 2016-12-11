#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: IcySun
# 脚本功能：分析apache日志 统计高频IP 和高频url

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import Counter
import os

path = 'F:/log/'
ipcount = []
urlcount = []
def use():
    print '#' * 50
    print '\t Analysis Logs For Apache'
    print '\t\t Code By: IcySun'
    print '#' * 50

def getcount(path):
    for root, dirs, files in os.walk(path):
        for fn in files:
            logname = root+'/'+fn

            for x in open(logname).readlines():
                ip = x.split(' ')[0]
                url = x.split(' ')[6]
                ipcount.append(ip)
                urlcount.append(url)

            iplist = Counter(ipcount)
            urllist = Counter(urlcount)
            print '======正在分析的日志：%s======' % fn
            for ip,count1 in iplist.most_common(5):
                print '[+] 访问IP: %s ,访问次数: %d' % (ip,count1)

            for url,count2 in urllist.most_common(10):
                print '[+] 访问URL: %s ,访问次数: %d' % (url,count2)

def main():
    use()
    getcount(path)

if __name__ == '__main__':
    main()