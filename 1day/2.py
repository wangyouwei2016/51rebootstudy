#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d", time.localtime())
riqi = time.strftime("%Y_%m_%d", time.localtime())
logname = ('/home/wangyw/access_log-%s.log' %(riqi))
print logname