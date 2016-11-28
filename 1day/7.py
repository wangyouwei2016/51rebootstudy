#!/usr/bin/python  
# -*- coding: utf-8 -*-  

# http://blog.csdn.net/onlyanyz/article/details/45177643  参考的算法讲解
# 选中 ctrl+/ 批量注释  pycharm技巧
#作业1 统计最大两个值
#方法1
unsortedList=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]


def bubbleSort(unsortedList):
    list_length = len(unsortedList)
    for i in range(0, list_length - 1):
        for j in range(0, list_length - i - 1):
            if unsortedList[j] > unsortedList[j + 1]:
                unsortedList[j], unsortedList[j + 1] = unsortedList[j + 1], unsortedList[j]
    return unsortedList
print bubbleSort(unsortedList)[-2:]

#方法2
unsortedList=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for i in sorted(unsortedList)[-2:]:
    print i

#作业2 统计字符出现次数
#参考 http://www.jb51.net/article/53911.htm
#方法1：
mylist = [1,2,2,2,2,3,3,3,4,4,4,4]
myset = set(mylist)  #myset是另外一个列表，里面的内容是mylist里面的无重复项
print myset
for item in myset:
  print("the %d has found %d" %(item,mylist.count(item)))
#方法2
List=[1,2,2,2,2,3,3,3,4,4,4,4]
a = {}
for i in List:
    if List.count(i) >= 1:
        a[i] = List.count(i)
print (a)

#方法3
from collections import Counter
print Counter([1,4,2,4,2,2,5,2,6,3,3,6,3,6,6,3,3,3,7,8,9,8,7,0,7,1,2,4,7,8,9])

#count函数 统计指定字符出现次数

x = "I like to program in Python"
print x.count("i")

#连加1+2+3到100
num = 0
for i in range(1,101):
    num += i
    print num