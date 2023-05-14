#write a program to find max of 3 numbers

#a=10; b=12; c=13
#a = int(input("Enter first integer as input: "))
#b = int(input("Enter second integer as input: "))
#c = int(input("Enter third integer as input: "))
#if a>b and a>c:
#    print(a, "is greater than",b,"and",c)
#elif b>a and b>c:
#    print(str(b)+" is greater than "+str(a)+" and "+str(c))
#else:
#    print(c, "is greater than",a,"and",b)

a=342
b=342
c=43
print(a,b,c,sep="|")
print(f"value of a: {a} value of b: {b} value of c: {c}")

x=5
y=3
z=x/y
print("value of z:  %0.2f"%(z))
print(f"value of z:  {z:0.2f}")

print("value of a: {0:0.2f} value of b: {1:0.2f} value of c: {2:0.2f}".format(a,b,c))

print("hello",end=" ")
print("welcome")

#for one line comment
a="this is a string"
b='''this is a a very 
big big big sring'''

'''this is a multi line string
working as multiline comment'''

#Operators in python
#a=3
if(a:=3)>5: #walrus operator
    print("a is greater")
else:
    print("a is smaller")

s=5
print(s)
print(s:=5) #assign and use 5


s="abc "
print(s*3)

a=4
b=5
c=b//a #ignores the decimal values

#Ternary operator in python
# c=a>b?a:b #java
c=a if a>b else b #pythonic

#Logical operators in python are and or not
#Bitwise operators in python & , |, >>, <<, ^

a=9
b=13
print(bin(a))
print(bin(b))

#compression
d=a<<4
print(bin(d))
x=d|b
print(bin(x),x)

print("and mask",int(0b1111))
#decompression
b=x&int(0b1111)
print("b",b)
a=x>>4
print("a",a)

#Loops in python

#range 1 to 10
for i in range(10):
    print(i,end=" ")
print()

#range 2 to 10
for i in range(2,10):
    print(i,end=" ")
print()

#increment by 2
for i in range(0,10,2):
    print(i,end=" ")
print()

#factorial
'''
num=int(input("enter number: "))
f=1
for i in range(1,num+1):
    f=f*i
print(f)

'''
#accept a number from user check whether it is prime of not
#for else loop
'''num=int(input("enter number: "))
if num == 1:
    print("is not a prime")
for i in range(2, num):
    if (num % i) == 0:
        print("is not prime")
        # break out of loop
        break
else:
    print("is prime")'''

# sum of digits
'''
num=int(input("enter number: "))
s=0
while num > 0:
    d=num%10
    num=num//10
    s=s+d
print("sum of digit is ",s)

'''

#to accept number from user untill they enter q
'''
num=0
sum=0
while True:
    num=input("enter number:")
    if num == "q":
        break
    if int(num) % 2 == 0:
        sum = sum + int(num) 
print(sum)
       
''' 

#match-case in python
'''
choice=int(input("enter number between 1 to 5: "))
match choice:
    case 1:
        print("you selected 1")
    case 2:
        print("you selected 2")
    case 3|4|5:
        print("you selected 3 to 5")
    case _:
        print("you selected greater than 5")

'''
'''
#calendar
days=int(input("enter number of days in a month"))
if days==30 or days==31 or days==29 or days==28:
    startday=int(input("enter startday monday-0 tuesday=1..."))
    print("mon\ttue\twed\tthu\tfri\tsat\tsat")
    cnt=startday
    print("   \t"*startday,end="")
    for i in range(1,days+1):
        print(f"{i}\t",end="")
        cnt=cnt+1
        if cnt%7 == 0:
            print()
            cnt=0

else:
    print("not valide no of days")
'''
#functions in python

def factorial(num=5):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f
def addition(x=1,y=2):
    return x+y

def printTable(num):
    for i in range(1,11):
        print(f"{i} {num}={i*num}")

choice =0
while choice !=4:
    choice=int(input("""1.factorial
                     2.add numbers
                     3.print table
                     choice"""))
    match choice:
        case 1:
            num=int(input("enter number for factorial"))
            ans=factorial(num)
            print(f"Factorial:{ans}")
        case 2:
            num1=int(input("enter number1 for adding"))
            num2=int(input("enter number2 for adding"))
            ans=addition(num1,num2)
            print(f"addition: {ans}")
        case 3:
            num=int(input("enter number for table"))
            printTable(num)
        case 4:
            print("bye")
        case _:
            print("wrong choice")
