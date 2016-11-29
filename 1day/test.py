#!/usr/bin/python  
# -*- coding: utf-8 -*-
# int格式化字符串为数字
from __future__ import print_function

num = 1
string = "3"
num2 = int(string)
print (num + num2)

# len统计个数
word = 'a loooooong word'
num = 12
string = 'bang!'
total = string * (len(word) - num)
print(total)

# 列表切片
phone_number = '13709821410'
hiding_number = phone_number.replace(phone_number[:7] , '*' * 9)
print hiding_number

# str格式化数字为字符串
search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print (search + ' is at ' + str(num_a.find(search)) + 'to' + str(num_a.find(search) + len(search)) + 'of num_a')

# format字符串批处理
print ('{} add {}.').format('wei' , 'wang')
print('{preposition} a word she can get what she {verb} for'.format(preposition='With' , verb='came'))
print('{0} a word she can get what she {1} for.'.format('With' , 'came'))


# city = input("write down the name of city:")  #int 输入数字
# url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
# print url

# 函数

def fahrenheit_converter(C):
    fahrenheit = C * 9 / 5 + 32
    return str(fahrenheit) + ' ̊F'


C2F = fahrenheit_converter(35)
print C2F

w = raw_input('please input wight(g):')


def wight_converter(w):
    kg = int(w) / 1000
    return str('The right triangle third side\'s lenght is %.3f' % kg) + 'KG'


print(wight_converter(w))


# 设计一个函数 控制写入文件名称和内容

def text_create(name,msg):
    desktop_path='/home/wangyw/ '
    full_path=desktop_path + name +'.txt'
    file.write(msg)
    file.close()
    print Done
text
