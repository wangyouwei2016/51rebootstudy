#!/usr/bin/python  
# -*- coding: utf-8 -*-  
# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# # for i in range(1,10):
# #     for j in range(1,10):
# #         print ('{}X{}={}'.format(i,j,i*j))
# #
# # num_arr = [1,2,3,4,5,6,7,8,9]
# #
# # for i in range(1, 10):
# #     for j in range(1, i+1):
# #         k = i * j
# #         print '%s * %s = %s ' % (i, j, k),
# #     print ''
# #
# #
# #
# # aList = [123, 'xyz', 'zara', 'abc'];
# #
# # print "Index for xyz : ", aList.index( 'xyz' ) ;
# # print "Index for zara : ", aList.index( 'zara' ) ;
# #
# # your_choice = int(raw_input('please input :'))
# # arr = [1,2,3,7,11,22]
# # print len(arr)
# # if your_choice in arr:
# #     print "index for your_choice: ", arr.index(your_choice)
# # else:
# #     print 'not in arr'
#
#
# ##二分法
# arr = [1 , 3 , 7 , 10 , 22 , 100 , 299 , 1000 , 2000 , 30000 , 40000]
# num1 = int(raw_input("please input a number:"))
# suy = 0
#
# mid = arr[len(arr) / 2]
# if num1 < mid:
#     for i in range(len(arr) / 2):
#         if arr[i] == num1:
#             print "you input number's suoying is %s" % suy
#         elif arr[i] < num1 and arr[i + 1] > num1:
#             print "you input number's suoying is before %s and %s" % (i , i + 1)
#         elif arr[len(arr) - 1] < num1:
#             print "you input number not in the list "
#             break
# else:
#     for i in range(len(arr) / 2 , len(arr)):
#         if arr[i] == num1:
#             print "you input number's suoying is %s" % suy
#         elif arr[i] < num1 and arr[i + 1] > num1:
#             print "you input number's suoying is before %s and %s" % (i , i + 1)
#         elif arr[len(arr) - 1] < num1:
#             print "you input number not in the list "
#             break

# arr1 =[1,2,2,2,3,4,5,322]
# arr2 =[1,2,2,2,3,4,5,44,55,66,1322]
# arr = arr1+arr2
# blist=[]
# clist=[]
# for i in arr1:
#     if i not in arr2

# print 'hello,reboot:yuou,xxx,xxx:xxx'.replace(',',':').split(':')
# f=open('/home/wangyw/1.txt')
# arr f.read().split('\n')
# f.close

user = raw_input('user:')
pwd = raw_input('pwd:')
f=open('/home/wangyw/1.txt')
arr = f.read().split('\n')
f.close

user_exists = False
for u in arr:
    temp = u.split(':')
    if temp[1] == user or temp[0]==user:
        if temp[2]==pwd:
            msg = 'success'
        else:
            msg = 'wrong'
        user_exists=True
        print msg
        break
if not user_exists:
    print 'user not exits'