# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# # int格式化字符串为数字
# from __future__ import print_function
#
# num = 1
# string = "3"
# num2 = int(string)
# print (num + num2)
#
# # len统计个数
# word = 'a loooooong word'
# num = 12
# string = 'bang!'
# total = string * (len(word) - num)
# print(total)
#
# # 列表切片
# phone_number = '13709821410'
# hiding_number = phone_number.replace(phone_number[:7] , '*' * 9)
# print hiding_number
#
# # str格式化数字为字符串
# search = '168'
# num_a = '1386-168-0006'
# num_b = '1681-222-0006'
# print (search + ' is at ' + str(num_a.find(search)) + 'to' + str(num_a.find(search) + len(search)) + 'of num_a')
#
# # format字符串批处理
# print ('{} add {}.').format('wei' , 'wang')
# print('{preposition} a word she can get what she {verb} for'.format(preposition='With' , verb='came'))
# print('{0} a word she can get what she {1} for.'.format('With' , 'came'))
#
#
# # city = input("write down the name of city:")  #int 输入数字
# # url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
# # print url
#
# # 函数
#
# def fahrenheit_converter(C):
#     fahrenheit = C * 9 / 5 + 32
#     return str(fahrenheit) + ' ̊F'
#
#
# C2F = fahrenheit_converter(35)
# print C2F
#
# w = raw_input('please input wight(g):')
#
#
# def wight_converter(w):
#     kg = int(w) / 1000
#     return str('The right triangle third side\'s lenght is %.3f' % kg) + 'KG'
#
#
# print(wight_converter(w))
#
#
# for num in range(1 , 11):
#     print str(num) + ' + 1 =' , num + 1
#
# songlist=['tes','aa','bb']
# for song in songlist:
#     if song == 'tes':
#         print song,'-daa'
#
# #循环嵌套
# for i in range(1,10):
#     for j in range(1,10):
#         print ('{}X{}={}'.format(i,j,i*j))
#
# count = 0  #目的是计数
# while True:
#     print('Repeat this line !')
#     count = count + 1
#     if count == 5:
#         break
#
# # 桌面生成10个文件
# for i in range(1,11):
#     full2_path = path + str(i) + '.txt'
#     file = open(full2_path,'w')

# #计算福利
# def invest(amount,rate,time):
#     print ("principal amount:{}".format(amount))
#
#     for t in range(1,time+1):
#         amount = amount*(1+rate)
#         print 'year {}: ${}'.format(t,amount)
#
# invest(100,2,4)
#
# #打印100内偶数
#
# for i in range(1,101):
#     if i % 2 == 0:
#         print i

# 摇色子游戏
# import random
#
#
# def roll_dice(number=3 , points=None):
#     print('<<<<<<<<<<<ROLL THE DICE>>>>>>>>>>>>>')
#     if points is None:
#         points = []
#     while number > 0:
#         point = random.randrange(1 , 7)           #注意是point 无s
#         points.append(point)                            #注意是point 无s
#         number = number - 1
#     return points
#
#
# def roll_result(total):
#     isBig = 11 <= total <= 18
#     isSmall = 3 <= total <= 10
#     if isBig:
#         return 'Big'
#     elif isSmall:
#         return 'Small'
#
#
# def start_game():
#     your_money = 1000
#     while your_money > 0:
#         print ('<<<<<game start>>>>>')
#         choices = ['Big' , 'Small']
#         your_choice = raw_input('Big or Small :')
#         if your_choice in choices:
#             your_bet = int(input('how much you wangna bet?-'))
#             points = roll_dice()
#             total = sum(points)
#             youWin = your_choice == roll_result(total)
#             if youWin:
#                 print ('The points are' , points , 'You win!')
#                 print ('you gaiend {},you have {} now!'.format(your_bet,your_money+your_bet))
#                 your_money=your_money+your_bet
#             else:
#                 print ('The points are' , points , 'You lose!')
#                 print ('You lose {},you have {} now'.format(your_bet,your_money-your_bet))
#                 your_money=your_money - your_bet
#         else:
#             print ('INVALID WORDS')
#     else:
#         print ('game over')
# start_game()


a = [letter.lower() for letter in 'ABCDEFGHIGKLMN']
print a
b = [n for n in range(1 , 10) if n % 2 == 0]
print b
d = {i: i + 1 for i in range(4)}
print d
