# def text_create(name , msg):
#     desktop_path = '/home/wangyw/ '
#     full_path = desktop_path + name + '.txt'
#     file = open(full_path , 'w')
#     file.write(msg)
#     file.close()
#     print 'Done'
#
#
# text_create('1AAA' , 'wwwwww')

path = '/home/wangyw/'
for i in range(1,11):
    full2_path = path + str(i) + '.txt'
    file = open(full2_path,'w')