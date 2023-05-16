#packing of tuple
x=1,2,3 
'''
x[0]=1

'''
#unpacking of tuple
p,q,r=x

a=12
b=23
print("before swapping ", a,b)
b,a=a,b #swapping of the number
print("after swapping",a,b)

#returning multiple values from a function, althought it is returning one tuple
def f1(x,y):
    x=x+10
    y=y+20
    return x,y

#default parameter
def f2(a,b=56,c=34):
    print(a,b)
    a=a+45
    print(a,b)

#addition accepts 1 mandator parameter, 2 optional parameter
#and in t variable number of parameter t is of type tuple
#default parameter for more than 3 values
def addition(a,b=10,c=3,*t): #*t is tuple for more than three parameter
    s=a+b+c
    for val in t:
        s=s+val
    return s
print("addition1",addition(10))
print("addition2",addition(2,5))
print("addition2",addition(2,4,5,6,3,5,7,5))



#f2(2,)
a=20 
b=30
p,q=f1(a,b)


#zip will help in traversing multiple lists
lst=[1,2,3]
lst1=["pune","mumbai","doon","ireland","iceland"]
for v,p in zip(lst,lst1): #[(1,"pune"),(2,"mumbai")..]
    print(v,"--->",p)


#search value in the list
lst=[12,1,3,14]
s=3
cnt=0
for v in lst:
    if v==s:
        print(v,cnt)
        break
    cnt=cnt+1

#or

#enumerate list starting with 0
lst=[12,1,3,14]
s=3
for idx,v in enumerate(lst): #[(0,12),(1,1),(2,3)]
    if v==s:
        print(v,idx)
        break

#or
#enumerate list starting with 1
lst=[12,1,3,14]
for idx,v in enumerate(lst,1): #[(0,12),(1,1),(2,3)]
        print(idx,":",v)

#reverse the list without changing the original list
for v in reversed(lst):
    print(v)
print(lst)

#sort the list without changing the original list(ASC)
for v in sorted(lst):
    print(v)
print(lst)

#sort the list without changing the original list(DSEC)
for v in sorted(lst,reverse=True):
    print(v)
print(lst)

lst=[12,12,14,1,2,3,4,15]
lst2=[]
for v in lst:
    if v%4==0:
        lst2.append(v)
print(lst2)

#list compression operator
lst3=[v for v in lst if v%4==0 and v>5]
print(lst3)

#lambda function 
lst4=list(filter(lambda x : x%4 == 0 and x>5,lst))


#
lst=[12,13,14,16,2,3,4,15]
lst1=[]
for i in lst:
    lst1.append(i**2)
print(lst1)

#or
lst2=[i**2 for i in lst]
print(lst2)

lst3=list(map(lambda x:x*x,lst))

from functools import reduce

ans=reduce(lambda x,y:x+y,lst)
print("answer: ",ans )

ans=reduce(lambda x,y:min(x,y),lst)
print("answer min: ",ans)

lst3=["python","perl","os","c++","java"]
ans=reduce(lambda x,y:x if len(x) < len(y) else y,lst3)
print(ans)
















