password1_list=['12345','000000','999']
def account_login():
    password1 = input('pass:')
    password1_correct = password1 == password1_list[:1]
    password1_reset = password1 == password1_list[-1]
    if password1_correct:
        print 'ok'
    elif password1_reset:
        new_password = input('enter a new:')
        password1_list.append(new_password)
        print 'update'
        account_login()
    else:
        print 'wrong'
        account_login()
account_login()