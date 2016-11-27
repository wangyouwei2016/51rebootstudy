js_count=0
for name in ['c','js','py','js']:
    if name=='js':
        js_count +=1
print js_count

max_num =0
for i in [1,2,3,4,4,5,777,6666,999]:
    if i>max_num:
        max_num=i
print max_num



for i in [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]:
    if i > max_num1:
        max_num1=i
print(max_num1)


unsortedList=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
print sorted(unsortedList)[-2:]

