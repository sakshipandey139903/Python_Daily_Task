#Tuple In Python
num=(10,20,30,40,50)
print(num)
tup=("Python","Cyber Security","Mysql")
print(tup)
info=("Sakshi",20,85.5,True)
print(info)
tup=()
print(tup)
print(type(tup)) # It is print a empty tuple like ()
num=(10,)
print(num)
print(type(num)) # Single element tuple me comma(,) improtant h

#Indexing In Tuple
lang=("Python","C++","Java","SQL")
print(lang[0])
print(lang[2])
print(lang[-1])

lang=("Python","C++","Java","SQL")
print(lang[-1])
print(lang[-2])
print(lang[-3])

col=("Red","Green","Blue","Yellow","Black")
print(col[0])
print(col[-1])
print(col[2])
print(col[-2])

#Slicing In Tuple
num=(10,20,30,40,50)
print(num[0:3])  #(10,20,30)
num=(10,20,30,40,50)
print(num[-3:]) #(30,40,50) last ending element 
num=(10,20,30,40,50)
print(num[1:4]) #(20,30,40)
num=(10,20,30,40,50)
print(num[:4])  #first four element (10,20,30,40)
num=(10,20,30,40,50)
print(num[-2:])
num=(10,20,30,40,50)
print(num[::-1])  # for reverse 

# Step slicing in tuple
num=(10,20,30,40,50,60)
print(num[0:6:2])   #(10,30,50)
num=(10,20,30,40,50,60)
print(num[1:6:2])  #(20,40,60)
#Reverse slicing
num=(10,20,30,40,50,60)
print(num[5:0:-2])


num=(10,20,30,40,50,60)
print(num[:4])
print(num[-3:])
print(num[1:4])
num=(10,20,30,40,50)
print(num[0:6:2])
num=(10,20,30,40,50,60)
print(num[5:0:-2])  #(60,40,20)

#Tuple Methods
num=(10,20,10,30,10,40)
print(num.count(10))  #3
colors=("Red","Blue","Red","Green","Red","Blue")
print(colors.count("Red"))
print(colors.count("Blue"))
num=(10,20,30,40,50)
print(num.index(40))  #3
num=(10,20,30,20,40,20)
print(num.index(20))  #1
num=(10,20,10,30,20,10,40)
print(num.count(10)) #3
print(num.index(20)) #1
print(num.index(30))#3


num=(10,20,30,20,40,10,50)
print(num)
print(num.count(20))
print(num.index(40))


colors=("Red","Green","Blue","Yellow","Black","Whhite")
print(colors[0])
print(colors[-1])
print(colors[0:3])
print(colors[-2:])

num=(10,20,30,40,50,60)
print(num[0:6:2])
print(num[5:0:-2])

data=("Python",20,"Cyber",20,30,"Python")
print(data)
print(data.count("Python"))
print(data.index(20))
print(data[0:3])
print(data[-2:])

num=(5,10,15,20,25,30,10)
print(num.count(10))
print(num.index(20))
print(num[0:4])
print(num[-3:])
print(num[::-1])

#Tuple Packing
lang=("Python","Mysql","Cyber Security")
print(lang)  #('Python','Mysql','Cyber Security')
#Tuple Unpacking
lang = "Python","Java","C++"
print(lang)
print(type(lang)) #('Python','Java','C++') < class 'tuple'>
# Ye dono hi tuple h
lang=("Python","Java","C++")
a,b,c=lang
print(a) #Python
print(b) #Java
print(c) # C++

student=("Sakshi",20,85)
name,age,marks=student
print(name) #'Sakshi'
print(age) # 20
print(marks) #85

data=("Python",20,"Cyber Security",85)
a,b,c,d=data
print(a)  #'Python'
print(b)  #20
print(c)  # 'Cyber Security'
print(d)  # 85
print(type(b)) # < class 'int'>

#SET IN PYTHON
num={10,20,30,40,50}
print(num)
num={10,20,10,30,20,40}
print(num)  # {10,20,30,40} It removes a duplicate values
info={"Python",20,85.5,True}
print(info)
emp=set()
print(emp)    #It's print a empty set
print(type(emp))
leng={"Python","Java","Python","C++","Java"}
print(leng)
num={5,10,15,10,20,5,25}
print(num)  #{5,10,15,20,25}
print(type(num)) #<class = 'set'>

#SET METHODS
num={10,20,30}
num.add(40)
print(num)
language={"Python","Java"}
language.add("C++")
print(language)

num={10,20,30,40}
num.remove(20)
print(num)
colors={"Red","Green","Blue","Yellow"}
colors.remove("Blue")
print(colors)
num={5,10,15,20,25}
num.remove(15)
print(num)
language={"Python","Java","C++","Mysql"}
language.remove("Java")
print(language)

num={10,20,30}
num.add(40)
print(num)
colors={"Red","Green","Blue","Yellow"}
colors.remove("Green")
print(colors)
num={10,20,30,40}
num.discard(50)
print(num)   # No error
num={10,20,30,40}
x=num.pop()
print(x)  
print(num)
num={10,20,30,40,50}
num.clear()
print(num)  #set()
print(type(num))  #<class='set'>

num={10,20,30}
num.add(40)
num.remove(20)
num.discard(50)
x=num.pop()
print(x)
print(num)

A={10,20,30}
B={30,40,50}
result=A.union(B)
print(result)  #{10,20,30,40,50}

set1={"Python","Java"}
set2={"C++","Python","Sql"}
set=set1.union(set2)
print(set)  #{Pyhon,Java,C++,sql}

a={1,2,3}
b={3,4,5}
c={5,6,7}
result=a.union(b,c)
print(result)  #{1,2,3,4,5,6,7}

a={10,20,30,40}
b={30,40,50,60}
result=a.union(b)
print(result) #{10,20,30,40,50,60} sets ki unique values

a={10,20,30}
b={20,30,40}
result=a.intersection(b)
print(result) #{20,30} dono set ki commob values

a={"Python","Java","C++"}
b={"Java","Sql","Python"}
result=a.intersection(b)
print(result)

a={10,20,30,40}
b={30,40,50,60}
print(a.difference(b))  #{10,20}

a={10,20,30}
b={20,30,40}
print(b.difference(a))  #{40}

a={"Pyhthon","Java","C++"}
b={"Java","Sql"}
print(a.difference(b))  #{"Python",C++}

a={10,20,30,40,50}
b={20,40,60}
print(b.difference(a))





text=input("Enter the string: ")
count=0
for ch in text:
    if ch in "aeiou":
        count=count+1
print("Total voweles",count)        


text=input("Enter the string: ")
count=0
for ch in text:
    if ch in " ":
        count=count+1
print("Total space",count)        


text="Hello Python"
count=0
for ch in text:
    if ch.isdigit():
        count=count+1
print("Total digit",count)    

text="Python123"
count=0
for ch in text:
    if ch.isdigit():
        count=count+1
print("Total digit",count)       

text="Hello PYTHON"
count=0
for ch in text:
    if ch.isupper():
        count=count+1
print("Total upper letters",count)        


text="Python is easy"
count=0
for ch in text:
    if ch.split():
        count=count+1
print("Total words",count)        













num=[15,45,22,60,35,10,80]
new_list=[]
for i in num:
    if i > 30:
        new_list.append(i)
print(new_list)


num=[8,12,15,20,25,32,40,45]
new_list=[]
for i in num:
    if i % 4 == 0:
        new_list.append(i)
print(new_list)


names=["Amit","Rahul","Neha","Priyanka","Rohit","Anjali"]
new_list = []
for i in names:
    if len(i) > 5:
        new_list.append(i)
print(new_list)  

       


num=[10,15,20,25,30,45,50,60,75]
new_list=[]
for i in num:
    if i%3==0 and i%5==0:
        new_list.append(i)
print(new_list) 



num=[10,-5,20,-8,30,-2,5]
new_list=[]
for i in num:
    if i < 0:
        new_list.append(0)
    else:
        new_list.append(i)
print(new_list)            

num=[12,17,20,25,30,41]
new_list=[]
for i in num:
    if i %2==0:
        new_list.append("Even")
    else:
        new_list.append("Odd")
print(new_list)            



employees = [
    {"name": "Amit", "salary": 55000},
    {"name": "Rahul", "salary": 70000},
    {"name": "Neha", "salary": 80000},
    {"name": "Rohit", "salary": 45000}
]
new_list=[]
for employee in employees:
    if employee ["salary"] > 60000:
        new_list.append(employee["name"])
print(new_list)        


employees = [
    {"name": "Amit", "department": "IT"},
    {"name": "Rahul", "department": "HR"},
    {"name": "Neha", "department": "IT"},
    {"name": "Rohit", "department": "Sales"}
]
new_list=[]
for employee in employees:
    if employee["department"]=="IT":
        new_list.append(employee["name"])
print(new_list)    



students = [
    {"name": "Aman", "marks": 65},
    {"name": "Priya", "marks": 80},
    {"name": "Riya", "marks": 72},
    {"name": "Karan", "marks": 55}
]
new_list=[]
for student in students:
    if student ["marks"] >= 70:
        new_list.append(student["name"])
print(new_list)        



employees = [
    {"name": "Amit", "department": "IT", "salary": 55000},
    {"name": "Rahul", "department": "HR", "salary": 70000},
    {"name": "Neha", "department": "IT", "salary": 80000},
    {"name": "Rohit", "department": "IT", "salary": 50000}
]
new_list=[]
for employee in employees:
    if employee["salary"] >=60000 and employee ["department"] == "IT":
        new_list.append(employee["name"])
print(new_list)   


students = [
    {"name": "Aman", "marks": 75, "stream": "Science"},
    {"name": "Priya", "marks": 85, "stream": "Arts"},
    {"name": "Riya", "marks": 70, "stream": "Science"},
    {"name": "Karan", "marks": 90, "stream": "Commerce"}
]
new_list=[]
for student in students:
    if student["marks"] >= 70 and student["stream"] == "Science":
        new_list.append(student["name"])
print(new_list)  





employees = [
    {"name": "Amit", "salary": 45000, "department": "IT"},
    {"name": "Rahul", "salary": 60000, "department": "HR"},
    {"name": "Neha", "salary": 48000, "department": "IT"},
    {"name": "Rohit", "salary": 55000, "department": "Sales"}
]
new_list=[]
for employee in employees:
    if employee["salary"] > 50000 or employee["department"] == "IT":
        new_list.append(employee["name"])
print(new_list)        

students = [
    {"name": "Aman", "marks": 75, "stream": "Science"},
    {"name": "Priya", "marks": 80, "stream": "Science"},
    {"name": "Riya", "marks": 55, "stream": "Science"},
    {"name": "Karan", "marks": 70, "stream": "Commerce"},
    {"name": "Neha", "marks": 60, "stream": "Science"}
]
new_list=[]
for student in students:
    if student ["marks"] > 60 and student["marks"] <= 80 and student ["stream"] == "Science":
        new_list.append(student["name"])
print(new_list)        


employees = [
    {"name": "Amit", "salary": 45000, "department": "IT"},
    {"name": "Rahul", "salary": 60000, "department": "HR"},
    {"name": "Neha", "salary": 48000, "department": "IT"},
    {"name": "Rohit", "salary": 55000, "department": "Sales"},
    {"name": "Priya", "salary": 40000, "department": "HR"}
]
new_list=[]
for employee in employees:
    if employee ["salary"] < 50000 or employee ["department"] =="HR":
        new_list.append(employee["name"])
print(new_list)        