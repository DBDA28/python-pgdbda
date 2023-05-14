#1. Accept 10 integers from user and print their average value on the screen
'''
sum=0
for i in range(1,11):
    num=int(input(f"enter the {i} number: "))
    sum=sum+num
avg=sum/10 
print(f"average: {avg}")

'''

#2. Print the following patterns using loop :

#4. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

'''

cnt=0
prod=1
sum=0
while True:
    num=input("enter a number: ")
    if num == "q":
        break
    cnt=cnt+1
    prod=prod*int(num)
    sum=sum+int(num)
avg=sum/cnt 
print(f"average: {avg}")
print(f"product: {prod}")

'''
# 5. Given a number count the total number of digits in a number and also find sum of digits of the number
'''

num=int(input("enter number: "))
s=0
cnt=0
while num > 0:
    d=num%10
    num=num//10
    cnt=cnt+1
    s=s+d
print("sum of digit is ",s)
print("number of digit: ",cnt)

'''
#6. To display the cube of the number upto given an integer. If the given integer is 5, then display cube of 1 to 4

'''

num=int(input("enter a number:"))
for i in range(1,num):
    print(i*i*i)

'''

# 7. Accept 20 numbers from user and display sum of only even numbers.
'''
sum=0
for i in range(1,21):
    num=int(input(f"enter the {i} number: "))
    if i%2 == 0: 
        sum=sum+num
print("sum of even numbers is: ", sum)

'''

#8. Ask user number of terms to be generated of a series.
#generate numbers for the following series and find its addition
#[9 + 99 + 999 + 9999+……..]

'''num=int(input("enter number of terms"))
a=0
sum=0
for i in range(0,num):
    a=a*10+9
    sum=sum+a
    print(a,end=" + ")
print()
print("sum:",sum)
'''

#9
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=int(input("enter number"))
term=int(input("enter number of terms"))
s=1+x
f=1
print(f"1+{x}",end="")
for i in range(2,term):
    #f=factorial(i)
    f=f*i
    s=s+((x**i)/f)
    print(f"+{x}^{i}/{i}!",end="")
print("=Answer: ",s)

