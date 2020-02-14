# -*- coding: utf8 -*-

number = 30
if number < 10:
    print('크다')
elif number == 20:
    print('같다')
else:
    print('!!')

k=0
while(k<5):
    print(k)
    k+=1

u=1
while(u<=50):
    if((u%3!=0) and (u%5!=0)):
        print (u)
    else:
        pass
    u+=1


for i in range(1,11):
    print i


testList = ['number','double','integer','float']
check =0
while(check < len(testList)):
    if testList[check]=='integer':
        print ('찾았다')
    else:
        print ('몰라')
    check+=1

for check in testList:
    if check == 'integer':
        print('찾았다')
    else:
        print('못차자따')
    
result = 0
for i in range(1,31):  #이상, 미만
    result += i
print(result)


for i in range(11,111):
    if((i%2!=0)and (i%3!=0) and (i%5!=0) and (i%7!=0)):
        print i


def add(a,b):
    return a+b

print(add(3,4))

def add_Many(*args):
    result = 0
    for i in args:
        result = result +i
    return result

print(add_Many(1,2,3,4,5))


def factorial(num):
    result = 0
    if(num==0):
        return 1
    elif(num==1):
        return num
    else:
        result = num*factorial(num-1)
        return result

print(factorial(5))


