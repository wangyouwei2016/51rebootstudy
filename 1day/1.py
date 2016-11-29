#!/usr/bin/python
# -*- coding: utf-8 -*-
al=['ssss']
al.append('wefwa')
print al

#条件判断
password_list = ['000','12345']
def account_login():
    password=input('password:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    print password_list[-1]
    if password_correct:
        print 'secc'
    elif password_reset:
        new_password = input('enter a new pss:')
        password_list.append(new_password)
        print ('set suc')
        account_login()
    else:
        print "false"
        account_login()
account_login()