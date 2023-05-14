#Diamond pattern
'''
num=int(input("enter odd number"))
cnt=num//2
scnt=1
for i in range(cnt+1):
    print(cnt*" "+"*"*scnt)
    cnt=cnt-1
    scnt=scnt+2
scnt=num-2
cnt=1
for i in range(num//2):
    print(cnt*" "+"*"*scnt)
    scnt=scnt-2
    cnt=cnt+1

'''
#math function
'''

import math
print("ceil ",math.ceil(123.23))
print("floor ",math.floor(123.23))
print(round(123.23423442,2))

'''

#string slicing
'''

s="I am Voldemort"
print("last character",s[-1])
print("first character",s[0])
print("2 to 9",s[2:9])
print("even index character",s[::2])
print("odd index character",s[1::2])
print("revers string",s[::-1])

'''
'''
s="this is cat, cat is cute, where is your cat"
pos=s.find("cat")
print(pos)
pos=s.find("cat",pos+1)
print(pos)
'''

#write program to find all occurrences of the given string
'''
s="this is cat, cat is cute, where is your cat"
pos=s.find("cat")
while pos!=-1:
    print("position: ",pos)
    pos=s.find("cat",pos+1)
'''
'''
#upper and lower case

s="abc:pqr:xyz:test,try"
print(s.upper())
print(s.lower())

'''

'''

#string splitting
s="abc:pqr:xyz:test,try"
lst=s.split(":")
print(lst)
s1="|".join(lst)
print(s1)

s2=s.replace(":","|")
print(s2)

#replace only first occurrence
s2=s.replace(":","|",1)
print(s2)

'''
'''
#strip club
s="sssssaaa dddd fff this is string ddd fffllll"
print(s.strip("sad fl"))
print(s.rstrip("sad fl"))
print(s.lstrip("sad fl"))

accno="xxxx123xxxx"
print(accno.strip("x"))
'''

'''
s="this is a string#$ g123, test"
for ch in s:
    #if ch.isdecimal():
    #if ch.isalnum():
    if ch.isalpha():
        print(ch,end="")
'''

#string literals and immutability


#Data Structures
#1.List
#2.Tuple
#3.Set
#4.Dictionary
#5.Frozenset

#List
lst=[1,2,3,4,"xx",[10,20,30]]
print(lst[3])
print(lst[5][1])

lst.append(45)
lst.insert(2,100)
print(lst)
lst2=["aaa","bbb","ccc"]
lst.extend(lst2)
print(lst)

