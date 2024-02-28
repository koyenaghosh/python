# -*- coding: utf-8 -*-
"""OOP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ns5BoqhACFM9BxYRqIzlNYAdW0zxS3yK

###the main objective of OOP is GENERALITY TO SPECIFICITY
###OOP is a programming paradigm of creating your own datatypes
###OOP concepts:
1. Class
2. Object
3. Abstraction
4. Inheritance
5. Encapsulation
6. Polymorphism

Class is a blueprint.Class has two characteristic features- Data/property(called ATTRIBUTE) and Functions/behaviour(called METHOD)

**syntax to create an object**

object_name=class_name()

Pascal Case-- each word starts with a capital letter and is written without any space. for eg.-> HelloWorld

Snake Case-- words start with small letter
and separated with an underscore. for eg. hello_world
"""

L=[1,2,3]
print(type(L))

# list is a class and L is an object of the class 'list'

L.upper()

class Atm:
  #constructor-- a special function inside the class. the code inside this function gets executed without calling it explicitly

  #non- parameterised constructor(no input needed)
  def __init__(self):
      self.pin=''
      self.balance=0
      self.menu()
  def menu(self):
      user_input=input("""Hi! How Can I help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check Balance
            4. Press 4 to withdraw
            5. Press any other digit to exit\n""")
      if user_input=='1':
          #create pin
          self.create_pin()
          self.menu()
      elif user_input=='2':
          #change pin
          self.change_pin()
          self.menu()
      elif user_input=='3':
          #check balance
          self.balance_check()
          self.menu()
      elif user_input=='4':
          #withdraw
          self.withdraw()
          self.menu()
      else:
          print("BYE!")
  def create_pin(self):
      user_pin=input("enter your pin:")
      self.pin=user_pin
      self.balance=int(input("Enter balance:"))
      print("pin created successfully!")
  def change_pin(self):
      old_pin=input("enter your pin:")
      if old_pin==self.pin:
          new_pin=input("enter new pin:")
          self.pin=new_pin
          print("Pin changed successfully!")
      else:
          print("Invalid pin. try again!")
  def balance_check(self):
        user_pin=input("enter your pin:")
        if user_pin==self.pin:
          print(f"your balance is: {self.balance}")
        else:
          print("Invalid pin. try again!")
  def withdraw(self):
        user_pin=input("enter your pin:")
        if user_pin==self.pin:
          amount=int(input("Enter amount to be withdrawn:"))
          if amount<=self.balance:
            self.balance-=amount
            print(f"Amount withdrawn.\nCurrent balance: {self.balance}")
          else:
            print("insufficient money!!")
        else:
          print("Invalid pin. try again!")

obj=Atm()
#a function existing independently outside a class can be called as a funtion. but a function defined within a class is called a method.

#example:
L=[1,2,3]
len(L)  #len() is a function.
L.append(4)  #append() is a method of class <'list'>

#constructor's super power
class Temp:
  def __init__(self):
    print("hello!")
abc=Temp()

#Creating a new datatype--FRACTION

class Fraction:
  # parameterised constructor (needs input)
  def __init__(self,x,y):  #here 2 inputs are needed
    self.num=x
    self.den=y
  def __str__(self):
    return f"{self.num}/{self.den}"
  def __add__(self,other):
    new_num=self.num*other.den+other.num*self.den
    new_den=self.den*other.den
    return f"{new_num}/{new_den}"
  def __sub__(self,other):
    new_num=self.num*other.den-other.num*self.den
    new_den=self.den*other.den
    return f"{new_num}/{new_den}"
  def __mul__(self,other):
    new_num=self.num*other.num
    new_den=self.den*other.den
    return f"{new_num}/{new_den}"
  def __truediv__(self,other):
    new_num=self.num*other.den
    new_den=self.den*other.num
    return f"{new_num}/{new_den}"


  def convert_to_decimal(self):
    decimal_form=self.num/self.den
    print(decimal_form)




fr1=Fraction(5,6)
fr2=Fraction(3,7)


fr1.convert_to_decimal()
print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)
print(fr1/fr2)

"""### Write OOP classes to handle the following scenarios:

 - A user can create and view 2D coordinates
 - A user can find out the distance between 2 coordinates
 - A user can find find the distance of a coordinate from origin
 - A user can check if a point lies on a given line
 - A user can find the distance between a given 2D point and a given line
"""

#Creating a class for 2D co ordinate system.

class Point:

  def __init__(self,x,y):
    self.x_cod=x
    self.y_cod=y

  def __str__(self):
    return f"<{self.x_cod},{self.y_cod}>"
  def euclidean_dist(self,other):
    return ((self.x_cod-other.x_cod)**2 +(self.y_cod-other.y_cod)**2)**0.5
  def dist_from_origin(self):
    return self.euclidean_dist(Point(0,0))

p1=Point(10,10)
p2=Point(1,1)
print(p1.euclidean_dist(p2))
print(p1.dist_from_origin())

class Line:

  def __init__(self,A,B,C):
    self.A=A
    self.B=B
    self.C=C

  def __str__(self):
    return f"{self.A}x+{self.B}y+{self.C}=0"

  def point_on_line(line,point):
    if line.A*point.x_cod+line.B*point.y_cod+line.C==0:
      return "lies on the line"
    else:
      return "doesn't lie on the line"

  def shortest_dist(line,point):
      d=abs(line.A*point.x_cod+line.B*point.y_cod+line.C)/(line.A**2+line.B**2)**0.5
      return f"{d} is the shortest distance."
l1=Line(5,4,6)
p1=Point(2,3)
print(l1)
print(p1)
l1.point_on_line(p1)
l1.shortest_dist(p1)

"""## **How objects access attributes**"""

class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

  def greet(self):
    if self.country == 'india':
      print('Namaste',self.name)
    else:
      print('Hello',self.name)

# how to access attributes
p = Person('nitish','india')

p.name

# how to access methods
p.greet()

# what if i try to access non-existent attributes
p.gender

"""### Attribute creation from outside of the class"""

p.gender = 'male'
p.gender

"""### Reference Variables

- Reference variables hold the objects
- We can create objects without reference variable as well
- An object can have multiple reference variables
- Assigning a new reference variable to an existing object does not create a new object
"""

# object without a reference
class Person:

  def __init__(self):
    self.name = 'nitish'
    self.gender = 'male'

p = Person()
q = p

# Multiple ref
print(id(p))
print(id(q))
#p and q are reference variables

# change attribute value with the help of 2nd object
print(p.name)
print(q.name)
q.name = 'ankit'
print(q.name)
print(p.name)

"""###Pass by reference"""

class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function
def greet(person):
  print('Hi my name is',person.name,'and I am a',person.gender)
  p1 = Person('ankit','male')
  return p1

p = Person('nitish','male')
x = greet(p)  #an object of a particular class acts as an input of a function outside the class.
print(x.name)
print(x.gender)



"""# Mutable Objects"""

class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function
def greet(person):
  person.name = 'ankit'
  return person
p = Person('nitish','male')
print(id(p))
p1=greet(p)
print(id(p1))

#since both the memory addresses are same, we can conclude that python objects are mutable just like lists, dict etc

"""# Encapsulation"""

class Atm:
  #constructor-- a special function inside the class. the code inside this function gets executed without calling it explicitly

  #non- parameterised constructor(no input needed)
  def __init__(self):
      self.pin=''
      self.__balance=0
      #self.menu()

  def get_balance(self):    #getter
      return self.__balance

  def set_balance(self,new_balance):    #setter
      if  type(self.__balance) == type(new_balance):
          self.__balance=new_balance
          return self.__balance
      else:
        print("ERROR!!")

  def menu(self):
      user_input=input("""Hi! How Can I help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check Balance
            4. Press 4 to withdraw
            5. Press any other digit to exit\n""")
      if user_input=='1':
          #create pin
          self.create_pin()
          self.menu()
      elif user_input=='2':
          #change pin
          self.change_pin()
          self.menu()
      elif user_input=='3':
          #check balance
          self.balance_check()
          self.menu()
      elif user_input=='4':
          #withdraw
          self.withdraw()
          self.menu()
      else:
          print("BYE!")
  def create_pin(self):
      user_pin=input("enter your pin:")
      self.pin=user_pin
      self.__balance=int(input("Enter balance:"))
      print("pin created successfully!")
  def change_pin(self):
      old_pin=input("enter your pin:")
      if old_pin==self.pin:
          new_pin=input("enter new pin:")
          self.pin=new_pin
          print("Pin changed successfully!")
      else:
          print("Invalid pin. try again!")
  def balance_check(self):
        user_pin=input("enter your pin:")
        if user_pin==self.pin:
          print(f"your balance is: {self.__balance}")
        else:
          print("Invalid pin. try again!")
  def withdraw(self):
        user_pin=input("enter your pin:")
        if user_pin==self.pin:
          amount=int(input("Enter amount to be withdrawn:"))
          if amount<=self.__balance:
            self.__balance-=amount
            print(f"Amount withdrawn.\nCurrent balance: {self.__balance}")
          else:
            print("insufficient money!!")
        else:
          print("Invalid pin. try again!")

obj=Atm()

obj.get_balance()

obj.set_balance('hehehe')

obj.create_pin()

obj.withdraw()

"""#Collection of Objects"""

# list of objects
class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

p1 = Person('nitish','male')
p2 = Person('ankit','male')
p3 = Person('ankita','female')

L = [p1,p2,p3]

for i in L:
  print(i.name,i.gender)

# dict of objects
class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

p1 = Person('nitish','male')
p2 = Person('ankit','male')
p3 = Person('ankita','female')

d = {'p1':p1,'p2':p2,'p3':p3}

for i in d:
  print(d[i].gender)

"""##### Relationships among classes- aggregation and inheritance.

Aggregation (meaning 'has a relationship')
"""

class Customer:
  def __init__(self,name,gender,address):
    self.name=name
    self.gender=gender
    self.address=address

  def print_add(self):
    print(self.address.city,self.address.pin,self.address.state)


class Address:

  def __init__(self,city,pin,state):
    self.city=city
    self.pin=pin
    self.state=state

ad1=Address("Kolkata",743377,"WB")
cust1=Customer("Koyena","Female",ad1)
cust1.print_add()

#but if we make the variable 'city' private, aggregation can't access it.

class Customer:
  def __init__(self,name,gender,address):
    self.name=name
    self.gender=gender
    self.address=address

  def print_add(self):
    print(self.name,self.address.get_city(),self.address.pin,self.address.state)

  def edit_profile(self,new_name,new_city,new_pin,new_state):
    self.name=new_name
    self.address.edit_address(new_city,new_pin,new_state)

class Address:

  def __init__(self,city,pin,state):
    self.__city=city
    self.pin=pin
    self.state=state

  def get_city(self):
    return self.__city
  def edit_address(self,new_city,new_pin,new_state):
    self.__city=new_city
    self.pin=new_pin
    self.state=new_state
ad1=Address("Kolkata",743377,"WB")
cust1=Customer("Koyena","Female",ad1)
cust1.print_add()
cust1.edit_profile("Nilanjana","Lavasa",412112,"Maharashtra")
cust1.print_add()

"""#Inheritance


*  What is inheritance?
*  What exactly gets inherited


"""

#example

#parent class
class User:

  def __init__(self):
    self.name="Koyena"

  def login(self):
    print("login")


#child class
class Student(User):

  # def __init__(self):
  #   self.rollno=100
  # we do not need the constructor in this class because it gets inherited from parent class
  def enroll(self):
    print("enroll into the course")

u=User()
s=Student()
print(s.name)
s.login()

# constructor example

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 13)
s.buy() #accessible as it is a public method
s.price #error because 'price' is a pvt variable

# constructor example 2

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print ("Inside SmartPhone constructor")

s=SmartPhone("Android", 2)
s.brand #it will show an error because child class has a constructor
#and the constructor of parent class doesn't run
#and the attributes were not initiated.

class Parent:

    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num

class Child(Parent):

    def show(self):
        print("This is in child class")

son=Child(100)
print(son.get_num())
son.show()

class Parent:

    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num

class Child(Parent):

    def __init__(self,val,num):
        self.__val=val

    def get_val(self):
        return self.__val

son=Child(100,10)
#print("Parent: Num:",son.get_num())
print("Child: Val:",son.get_val())

class A:
    def __init__(self):
        self.var1=100

    def display1(self,var1):
        print("class A :", self.var1)
class B(A):

    def display2(self,var1):
        print("class B :", self.var1)

obj=B()
obj.display1(200)

# Method Overriding
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")

s=SmartPhone(20000, "Apple", 13)

s.buy()

"""# Super Keyword"""

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        # syntax to call parent class's buy() method
        super().buy()

s=SmartPhone(20000, "Apple", 13)

s.buy()

# super -> constuctor
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        print('Inside smartphone constructor')
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print ("Inside smartphone constructor")

s=SmartPhone(20000, "Samsung", 12, "Android", 2)

print(s.os)
print(s.brand)

#super() keyword only works inside a child class and not outside

#super() can't access variables but only methods of a class

"""Inheritance Summary


*   A class can inherit from another class
*  Inheritance improves code reusability
*   Constructor, attribute and methods can get inherited to the child class
*   Parent has no access to the child class
*  Private properties of parent class aren't directly accessible in child class.
*   child class can override the attributes or methods. this is called method overriding
*   super() is an inbuilt function which is used to invoke the parent class methods and constructor.






"""

# single inheritance
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()

# multilevel
class Product:
    def review(self):
        print ("Product customer review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()

# Hierarchical
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()
FeaturePhone(10,"Lava","1px").buy()

# Multiple
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def review(self):
        print ("Customer review")

class SmartPhone(Phone, Product):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy() #method of class 'Phone'
s.review()  #method of class 'Product'

# the diamond problem
# https://stackoverflow.com/questions/56361048/what-is-the-diamond-problem-in-python-and-why-its-not-appear-in-python2
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def buy(self):
        print ("Product buy method")

# Method resolution order
class SmartPhone(Phone,Product):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()

#in a conflicting situation in case of multiple inheritance where both the parent classses have methods with same name, we use the method wrt the order of the classes written .

class A:

  def m1(self):
    return 20

class B(A):
  def m1(self):
    return 30
  def m2(self):
    return 40

class C(B):
  def m2(self):
    return 20


obj1=A()
obj2=B()
obj3=C()
print(obj1.m1()+obj2.m1()+obj3.m2())

"""# Polymorphism

"""

#method overloading

class Shape:

  def area(self,radius):
      return 3.14*radius**2

  def area(self,length,breadth):
      return length*breadth

s = Shape()

print(s.area(2))
print(s.area(3,4))

#solving the problem of method overloading in above eg.

class Shape:

  def area(self,a,b=0):
    if b == 0:
      return 3.14*a*a
    else:
      return a*b

s = Shape()

print(s.area(2))
print(s.area(3,4))

"""# Abstraction"""

from abc import ABC,abstractmethod
class BankApp(ABC):

  def database(self):
    print('connected to database')

  @abstractmethod #decorator
  def security(self):
    pass

  @abstractmethod #decorator
  def display(self):
    pass

class MobileApp(BankApp):

  def mobile_login(self):
    print('login into mobile')

  def security(self):
    print('mobile security')

  def display(self):
    print('display')

mob=MobileApp()

obj=BankApp()

