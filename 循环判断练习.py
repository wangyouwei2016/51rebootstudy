#!/usr/bin/python  
# -*- coding: utf-8 -*-  
for num in range(1 , 11):
    print str(num) + ' + 1 =' , num + 1

songlist=['tes','aa','bb']
for song in songlist:
    if song == 'tes':
        print song,'-daa'

#循环嵌套
for i in range(1,10):
    for j in range(1,10):
        print ('{}X{}={}'.format(i,j,i*j))

count = 0  #目的是计数
while True:
    print('Repeat this line !')
    count = count + 1
    if count == 5:
        break

# 桌面生成10个文件
for i in range(1,11):
    full2_path = path + str(i) + '.txt'
    file = open(full2_path,'w')

def invest(amount,rate,time):
    print ("principal amount:{}".format(amount))

    # for time in range(1,time):
    #     amount = amount*(1+rate)*time

invest(100,2,4)

