
#4
'''
count=0
for i in range (100,1000):
    if (i%5==0 and i%6==0):
        print(i,' ',end="")
        i+=1
        count+=1
        if count%10==0:
            print(' ')
'''
#1
'''
number=eval(raw_input("Enter an integer,the input ends if it is 0:"))
a=0
b=0
c=0
d=0
while number!=0:
    if number>0:
        a=a+number
        c+=1
    else:
        b=b+number
        d+=1
    number=eval(raw_input("Enter an integer,the input ends if it is 0:"))
AVG1=a/c
AVG2=b/d
print('{},{}'.format(AVG1,AVG2))
'''
#2
'''
xf=10000
i=1
z=0
while i<15:
    xf=xf*(1+0.05)
    if i==10:
        print("ten years:{:.2f}".format(xf))
    if i>=10:
        z=z+xf
    i+=1
print("ten years+college four years:{:.2f}".format(z))
'''
#5
'''
x=0
y=0
while (x*x)<=12000:
    x+=1
print(x)
while (y*y*y)<=12000:
    y+=1
print(y-1)
'''















