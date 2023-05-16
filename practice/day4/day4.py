'''
s={1,2,3,4,5,1}
print(set)
#to convert string to set to remove the duplicate characters
s1=set("This is string")
print(s1)

#to convert list to set to remove the duplicate strings
s2=set(["python","java","os","os"])
print(s2)

print(s)
s.add(34)
s.add("xxx")
s.add((10,20,30,"vvv"))
#s.add([11,22,33]) #cannot add list to set
print(s)

#adding all vlaues of iterable object itno another set
s.update(s2)
print(s)

#to delete random value from the set
v=s.pop()
print(v)
print(s)

#to delete the given value
#s.remove("python")
print(s)

#ignore if doesn't exist
s.discard("python")

#set theory based functions for set data-structure
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A,B)
print("union of A and B",A|B)
print("intersection of A and B",A&B)
print("difference of A and B",A-B)
print("symmetric_difference of A and B",A^B)

print("difference_update of A and B")
A=A-B
print(A)

A={1,2,3,4,5}
B={4,5,6,7,8}
print("symmetric_difference_update of A and B")
A=A^B
print(A)


#superset
A={10,20,30,40}
B={10,20}
print("A is superset of B:",A.issuperset(B))
print("A is subset of B:",A.issubset(B))

#Disjoint
A={"a","b","c"}
B={1,2}
print("A is disjoint of B",A.isdisjoint(B))


#shallow copy of sets
s={1,2,3}
s1=s
s.add(23)
print(s,s1)
s2=s.copy()
s.add(5)
print(s,s1)
print(s2)


#Dictionary
D1={"a":23,"b":10}
D2={"b":30,"c":56}
D1.update(D2)
print(D1)

d1={"python":234,"java":456,"c":200}
#print all keys
print(d1.keys())
#print all values
print(d1.values())

#since the key is not present in the dict the below will add it
d1[".net"]=345
print(d1)

#since key exists it will over-write the value
d1["python"]=345

#if key is known then to retrieve the value if key exists
#otherwise throws exception
print(d1["python"])

#check if key exists by avoiding the exception
v=d1.get("python")
if v!=None:
    print("key found",v)
else:
    print("key not found")

#default value
v=d1.get("python3",-1)
if v!=-1:
    print("key found",v)
else:
    print("key not found")

v=d1.setdefault("python3",100)
print(d1)


d1={"python":333,".net":444,"c":555}
for k in d1.keys():
    print(k,"--->",d1[k])

for k in d1.items():
    if v>400:
        print(k,"--->",v)

d1={"a":10,"b":20}
d2={"b":40,"c":70}
d1.update(d2)
print(d1)

d1={"a":10,"b":20,"c":70,"d":56,"x":89}
#delete the last key->value pair
k,v=d1.popitem()
print(k,v) #"x" 89
print(d1)

#to delete the key-> vlaue pair if key exists otherwise -1
k="b"
v=d1.pop(k,-1)
print(k,"-->",v)
print(d1)
'''
#course management system program
courses={"DBDA":57,"DAI":50}

def addnewcourse():
    cname=input("enter new coursename")
    num=int(input("enter the number of participants"))
    v=courses.get(cname,-1)
    if v!=-1:
        courses[cname]=num
        return True
    else:
        return False

def displayall():
    for k,v in courses.items():
        print(f"{k}-->{v}")

def deletecourse(cname):
    v=courses.get(cname,-1)
    if v!=-1:
        ans=input(f"{cname}--> {v} delete y/n")
        if(ans=="y"):
            courses.pop(cname)
            return 1
        else:
            return 2
    else:
        return 3

def modifynumber(cname,num):
    v=courses.get(cname,-1)
    if v!=-1:
        ans=input(f"{cname}--> {v} modified {num} y/n")
        if(ans=="y"):
            #over-write the value of the key
            courses[cname]=num
            return 1
        else:
            return 2
    else:
        return 3

def modifyname(cname,newcname):
    v=courses.get(cname,-1)
    if v!=-1: 
        ans=input(f"{cname} to {newcname} y/n")
        if(ans=="y"):
            #delete course cname and return its value
            val=courses.pop(cname)
            #add a new key and value pair
            courses[newcname]=val
            return 1
        else:
            return 2
    else:
        return 3

def dispbynum(num):
    for k,v in courses.items():
        if v>num:
            print(f"{k}-->{v}")

while True:
    choice=int(input("""
    1. add new course
    2.delete the course
    3. modify number of participant of the course
    4. modify course name
    5. display all courses with number of participants are > 40
    6. display all courses
    7. display a particular course
    8. exit
    """))
    match choice:
        case 1:
            status=addnewcourse()
            if status:
                print("added successfully")
            else:
                print("duplicate course")
        case 3:
            cname=input("enter course name to modify participants")
            num=int(input("enter number of participants"))
            status=modifynumber(cname,num)
            if status==1:
                print("modified successfully")
            elif status==2:
                print("found but not modified")
            else:
                print("not found")

        case 4:
            cname=input("enter course name to delete")
            newcname=input("enter coursename to added")
            status=modifyname(cname,newcname)
            if status==1:
                print("modified successfully")
            elif status==2:
                print("found but not modified")
            else:
                print("not found")

        case 2:
            cname=input("enter course name to delete")
            status=deletecourse(cname)
            if status==1:
                print("deleted successfully")
            elif status==2:
                print("found but not deleted")
            else:
                print("not found")
        case 6:
            displayall()
        case 5:
            num=int(input("enter number of participants"))
            dispbynum(num)
        case 8:
            print("bye!")
            break
        case _:
            print("Invalid Input")













