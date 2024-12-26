# creating the defined and positional arguments

def greet(name="friend"):
    print("Hello",name,"!")
    print("Happy belated christmas!")

greet("Shuaib")
greet()

def add(a=1,b=2,c=3,d=4):
    print(a + b + c + d)

add(2,3,6,4)
add()