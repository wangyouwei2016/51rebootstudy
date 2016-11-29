#!/usr/bin/python  
# -*- coding: utf-8 -*-  
password_list = ['0000','12345']
print password_list[-1]
def account_login():
    password = input('Password:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    print password_correct
    if password_correct:
        print ('secc')
    elif password_reset:
        new_password = input('newone:')
        password_list.append(new_password)
        print ('updateok')
        account_login()
    else:
        print ('errorps')
        account_login()
account_login()

##以上py3好使