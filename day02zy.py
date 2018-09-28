#1.1
'''
import math
r=eval(raw_input("Enter the length from the center to a vertex:"))
s=2*r*(math.sin(math.pi/5))
Area=(5*s*s)/(4*(math.tan(math.pi/5)))
print('The area of the pentagon is {:.2f}'.format(Area))
'''
#1.2
'''
import math
x1,y1=eval(raw_input("Enter point 1(latitude and longitude) in degrees:"))
x2,y2=eval(raw_input("Enter point 2(latitude and longitude) in degrees:"))
radius=6371.01
x1=math.radians(x1)
x2=math.radians(x2)
y1=math.radians(y1)
y2=math.radians(y2)
part1=math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
d=part1*radius
print("The distance between the two points is {} km ".format(d))
'''
#1.3
'''
import math
s=eval(raw_input("Enter the side:"))
Area=(5*s*s)/(4*math.tan(math.pi/5))
print("The area of the pentagon is {}".format(Area))
'''
#1.4
'''
import math
n=eval(raw_input("Enter the number of sides:"))
s=eval(raw_input("Enter the side:"))
part1=n*s*s
part2=4*math.tan(math.pi/n)
Area=part1/part2
print("The area of the polygn is {}".format(Area))
'''
#1.5
'''
x=eval(raw_input("Enter an ASCII code:"))
y=chr(x)
print("The character is {}".format(y))
'''
#1.6
'''
name=str(raw_input("Enter employee's name:"))
hours=eval(raw_input("Enter number of hours worked in a week:"))
pay=eval(raw_input("Enter hourly pay rate:"))
ftax=eval(raw_input("Enter federal tax withholding rate:"))
stax=eval(raw_input("Enter state tax withholding rate:"))
G=hours*pay
F=G*ftax
S=G*stax
N=G-F-S
print("Employee Name:{}".format(name))
print("Hours Worked:{}".format(hours))
print("Pay Rate:${}".format(pay))
print("Gross Pay:${}".format(G))
print("Deductions:")
print("  Federal Withholding(20.0%):${}".format(F))
print("  State Withholding(9.0%):${:.2f}".format(S))
print("  Total Deduction:${:.2f}".format(F+S))
print("  Net Pay:${:.2f}".format(N))
'''
#1.7
'''
number=int(raw_input("Enter an integer:"))
a=number/1000
b=(number-(a*1000))/100
c=(number-(a*1000)-(b*100))/10
d=number-a*1000-b*100-c*10
number2=d*1000+c*100+b*10+a
print("The reversed number is{}".format(number2))
'''
#1.8
'''
res=' '
for i in "1329076463@qq.com":
    res=res+chr(ord(i)+2)
print(res)
'''
#1.8(2)
new text=''
for i in text:
    new = chr(ord(i)+1)
    new text =new text+new
print(new text)
with open('wohaihao','w') as f:
    f.write(new text)
#2.1
'''
import math
a,b,c=eval(raw_input("Enter a,b,c:"))
if (b*b-4*a*c)>0:
    r1=((-b)+math.sqrt(b*b-4*a*c))/(2*a)
    r2=((-b)-math.sqrt(b*b-4*a*c))/(2*a)
    print("The roots are{:.6f} and {:.5f} ".format(r1,r2))
elif (b*b-4*a*c)==0:
    r1=((-b)+math.sqrt(b*b-4*a*c))/(2*a)
    print("The root are {}".format(r1))
else:
    print("The equation has no real roots")
'''
#2.2
'''
import random
num1=random.randrange(0,100)
num2=random.randrange(0,100)
print("num1:{},num2:{}".format(num1,num2))
x=eval(raw_input("Enter a sum:"))
s=num1+num2
if x==s:
    print("True")
else:
    print("False")
'''
#2.3
'''
number1=eval(raw_input"Enter today is day:")
number2=eval(raw_input"Enter the number of days elapsed since today:")
s=(number1+number2)
    if s==0:
        return 'Sunday'
    elif s==1:
        return 'Monday'
    elif s==2:
        return 'Tuesday'
    elif s==3:
        return 'Wednesday'
    elif s==4:
        return 'Thursday'
    elif s==5:
        return 'Friday'
    elif s==6:
        return 'Saturday'
print("Today is {} and the future day is {}".format(number1,s))
'''
#2.4
'''
a,b,c=eval(raw_input("enter three number:"))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print(a,b,c)
'''
#2.5
'''
price1,weight1=eval(raw_input("Enter weight and price for package 1:"))
price2,weight2=eval(raw_input("Enter weight and price for package 2:"))
a=price1/weight1
b=price2/weight2
if a>b:
    print("Package 2 has the better price.")
else:
    print("Package 1 has the better price.")
'''
#2.6

#2.7
'''
import random
num=random.randint(0,1)
x=eval(raw_input("enter  0 or 1:"))
if x==num:
    print("True")
else:
    print("False")
'''
#2.8
'''
import random
num=random.randint(0,1,2)
x=eval(raw_input("scissor(0),rock(1),paper(2):"))
if num==0:
    '''
#2.10
'''
import random
a=random.choice(['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'])
b=random.choice(['flower','redpeach','square','blackpeach'])
print("The card you picked is the {} of {}".format(a,b))
'''
#2.11
'''
import math
number=eval(raw_input("Enter a three-digit:"))
a=number/100
b=number%10
if(a==b):
    print("{} is a palindrome".format(number))
else:
    print("{} is not a palindrome".format(number))
'''
#2.12
'''
import math
a,b,c=eval(raw_input("Enter three edges:"))
x=a+b
y=b+c
z=a+c
if x>c and y>a and z>b:
    print("The perimeter is:{}".format(a+b+c))
else:
    print("False")
'''







