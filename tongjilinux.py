#!/usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os

mem = {}
f = open("/proc/meminfo")
lines = f.readlines()
f.close()
for line in lines:
    if len(line) < 2: continue
    name = line.split(':')[0]
    var = line.split(':')[1].split()[0]
    mem[name] = long(var) * 1024.0
mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']

print (mem)


hd = {}
disk = os.statvfs("/opt")
hd['available'] = disk.f_bsize * disk.f_bavail
hd['capacity'] = disk.f_bsize * disk.f_blocks
hd['used'] = disk.f_bsize * disk.f_bfree
print hd