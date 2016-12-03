#!/usr/bin/python
# -*- coding: UTF-8 -*-
for i in range(1,10):
    for j in range(1,10):
        print ('{}X{}={}'.format(i,j,i*j))

num_arr = [1,2,3,4,5,6,7,8,9]

for i in range(1, 10):
    for j in range(1, i+1):
        k = i * j
        print '%s * %s = %s ' % (i, j, k),
    print ''



aList = [123, 'xyz', 'zara', 'abc'];

print "Index for xyz : ", aList.index( 'xyz' ) ;
print "Index for zara : ", aList.index( 'zara' ) ;

your_choice = int(raw_input('1-3 :'))
arr = [1,2,3]
if your_choice in arr:
    print "index for your_choice: ", arr.index(your_choice)
else:
    print 'not in arr'