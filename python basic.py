# print("hello world")

# print("Hello"+"\tpython") #concatenation of two strings

# #use ctrl+/ to select and comment out

# print("Hello\t"+input("Name?"))

# a=int(input("Enter the no. of students in your college: "))
# #inputs on the right side are assigned to the left side of the = sign

# # since python only takes str input, we use int() to convert the input value into integer.

# b=9
# print(a+b)

# print(len(input()))
# print(len(123) ) #integer has no length

#Q1: take input 12,41 and obtain output 41,12
# x=input("enter a number")
# print(x[3]+x[4]+"\t"+x[0]+x[1])

#apart from int, float and char there is another data type called BOOLEAN- TRUE, FALSE

# a=(len("hello"))
# print(type(a))

# #print("hello "+a+"is there")
# new_a=str(a)
# print("hello "+new_a+" is there")

# # ##Guess the output:
# print(70 + float("100.5"))  #output=170.5
# print(str(70) + str(100))  #output=70100

# ##Exercise

# #1. Write a program which takes a 3 digit input and returns the sum of those digits

# a = (input("enter a number with 3 digits:\t"))
# print(int(a[0])+int(a[1])+int(a[2]))

##2. Check whether a 3 digit input is palindrome or not.
# A=input("Enter a number:")
# if  A[0]==A[4]:
#     A[1]==A[3]:
#   print("the number is palindrome")
# else:
#   print(" not palindrome")

# print(3*(3+3)/3-3)

# #Calculate mean and sd of 4 nos. taken as input from the user
# a1=int(input("Enter a number:"))
# a2=int(input("Enter a number:"))
# a3=int(input("Enter a number:"))
# a4=int(input("Enter a number:"))
# x_bar=(a1+a2+a3+a4)/4
# print("mean is\t",x_bar)
# s=((a1-x_bar)**2+(a2-x_bar)**2+(a3-x_bar)**2+(a4-x_bar)**2)/4
# print("SD is\t",s)
# print(round(s,1))
# print("mean is",x_bar,"and sd is",s)

# print(f"mean is {x_bar} and SD is {s}")
# #f-string is used to print the info irrespective of any data type.

# #Ex1.Create a program using f-string that tells how many weeks are left till the completion of the course.
# # input- name,course duration, course completed till now

# name=input("Enter your name:")
# c1=int(input("Enter the duration of the course(in days): "))
# c2=int(input("Enter the time of course completed till now(in days): "))
# c3=c1-c2
# print(f"{name} has {c3} days left till the completion of the course.")

# #Ex2.  Make a python program where user is asked to :
# #1. what will be the total bill?
# #2. what % tip would you like to give?-10,12 or 15.
# #3. how many people are paying?
# # output should be the amount paid by each person.

# total bill=int(input("Enter the total bill:"))
# tip=float(input("Enter the tip percentage-10% or 12% or 15%:"))

# p=float(input("the % that you got: "))
# if  50<p<80:
#   print("you have been kept in the waiting list")
# elif p>80:
#   print("you are eligible for Python programming course")
# else:
#   print("you aren't eligible for the course.")

# Ex.4 write a program where user is asked whether he wants to take stats as a minor course?
# -yes/no. if marks>60%, he is eligible otherwise not.

# a=input("Do you want to take statistics as a minor course?-yes/no: ")
# marks=float(input("enter your percentage of marks in HS: "))
# if a=="yes":
#   if marks>60:
#     print("you are eligible for the course")
#   else:
#     print("you are not eligible for the course")
# else:
#   print("okay ")

#Ex.5 Write a program to check whether a year is leap or not.
# y =int(input("Enter a year:"))
# if y % 4 == 0:
#   print(f"{y} is a leap year")
# else:
#   print(f"{y} isn't a leap year")

# #Ex.6 Write a program to check whether a number is prime or not.

# x=int(input("Enter a number:"))
# for i in range(2,x):
#   if x%i!=0:
#     print(f"{x} is prime")
#     break
#   elif x%i==0:
#     print(f"{x} isn't prime")
#     break

##Ex.7 Take a number of any length and print the 2nd last digit.(hint: use % or //)
# z=input("Enter a number of any length:")
# l1=len(z)
# print(z[l1-2])

#Ex.8 Chicken biryani order automation.
#user will be asked whether he wants half /full plate. half plate = Rs. 100 and
#full plate = Rs. 150.if extra aloo is added, amount will be increased by Rs 10.
#for extra chicken, +Rs. 50, for extra egg +rs. 20.
#output : thank you for your order. you are charged with Rs. 200.

# print("Welcome! Here's the menu:\n1. Chicken Biryani(half):\tRs.100\n")
# print("2. Chicken Biryani(full):\tRs.150\n3. for extra aloo +Rs.10\n")
# print("4. for extra egg +Rs.20\n5. for extra chicken +Rs.50")

# i1=int(input("no. of full plate chicken biryani:"))
# i2=int(input("no. of half plate chicken biryani:"))
# i3=int(input("no. of extra piece of aloo:"))
# i4=int(input("no. of extra piece of egg:"))
# i5=int(input("no. of extra piece of chicken:"))
# S=((i1*150)+(i2*100)+(i3*10)+(i4*20)+(i5*50))
# print(f"thank you for your order!you are charged with Rs.{S}")

# RANDOMISATION
import random  #"random" is an inbuilt module

r=random.randint(1,10)
print(r)
import mymodule

print(mymodule.a)
print(mymodule.studentlist)
# When we define the module in order to access in it main.py, we use 'import <module name>'
# and to access any variable or function of the said module we use the format
# <module name.variable>

#Ex. Create a module to calculate the sum of 3 nos. and print the sum in main.py
# import sum

# print(sum.S)

# print(random.random()) #generates random numbers between 0 and 1 excluding 0 & 1
# print(random.uniform(2,5))
# print(random.bin(10,0.5))
# print(random.expovariate(0.5))

# print(4*random.random()+3*random.random())

#Ex. Write a code randomly telling user heads or tails.
import random
c1=input("head or tail?:")
c2=random.randint(0,1)
if c2==0:
  result='head'
if c2==1:
  result='tail'
print(f"User:{c1} and coin shows:{result}")
if c1==result:
  print("User won the toss")
else:
  print("User lost the toss")

#PYTHON LISTS - a part of data structure.
#studentlist=["A","B","C"]
# print(studentlist[0])
# studentlist.append("D")
# print(studentlist)
# studentlist.extend(["E","F"])
# print(studentlist)
# studentlist.remove("A")
# print(studentlist)

#Ex. Write a program that will select a random name from a list to sing a song.

import random

l=len(studentlist)
r=random.randint(0,l-1)
name=studentlist[r]
print(f"{name} will sing a song")

#Ex. Given the names and grades for each student in a class of n students. store them in a nested list.print the names of any student having the second lowest grade.
import random

input("Enter the number of students:")
names=list(input("Enter their names:").split())
grades=[int(x) for x in input("Enter their grades: ").split()]
print(names)
print(grades)
list=names+grades
print(list)
r=random.randint(0,5)
for i in range(1,r+1):
  if grades[i-1]<grades[i]:
    print(f"{list[r]} has the second lowest grade")
    break

#Ex. Built the game rock,paper,scissor.
# import random

print("ROCK PAPER SCISSOR GAME")
u=input("Enter any one: ")
c=random.randint(1,3)
if c==1:
  result='rock'
if c==2:
  result='paper'
if c==3:
  result='scissor'
print(f"User:{u}\nComputer:{result}")
if u==result:
  print("its a tie!play again")
elif u=='rock':
  if result=='scissor':
    print("User won!")
  if result=='paper':
    print("User lost!")
elif u=='scissor':
  if result=='paper':
    print("User won!")
  if result=='rock':
     print("User lost!")
elif u=='paper':
  if result=='scissor':
      print("User lost!")
  if result=='rock':
      print("User won!")

#NESTED LIST
#list1=[["Anjan",30],["Suman",40]]
#to access "Anjan" from list1 we use list[0][0]

#LOOPS
#for loop
# list=["A","B","C"]
# for i in list:
#   print(i)
# print(i +"\nenemy")

# for i in range(0,3):
#   S=0
#   S=S+i
#   i=i+2

#Ex. take 5 inputs of heights and calculate mean,median using loops.

h=[int(x) for x in input("Enter heights in cms of 5 persons:").split()]
print(h)
for i in h:
  S=0
  S=S+i
mean=S/5
print(mean)
list2=sorted(h)
print(list2)
l=len(list2)
if l%2==0:
    print(list2[l//2]+list2[l//2+1]/2)
else:
    print(list2[(l+1)//2])

n=input("no. of obs.")
list=[0]
for i in range(0,len(n)):
  x=int(input("Enter height:"))
  list.append(x)
print(list)
s=0
for i in list:
    s=s+i
mean=s/5
print(mean)

#Suggest a strong password
import random
import string

letters=list(string.ascii_lowercase)
#print(alphabet_list)
numbers=['0','1','2','3','4','5','6','7','8','9']
#print(numbers)
symbols=["!","@","#","_"]
nr_letters=int(input("letters:"))
nr_symbols=int(input("symbols:"))
nr_numbers=int(input("numbers:"))
password=[]
for char in range(1,nr_letters+1):
  random_char1=random.choice(letters)
  password.append(random_char1)
for char in range(1,nr_numbers+1):
  random_char2=random.choice(numbers)
  password.append(random_char2)
for char in range(1,nr_symbols+1):
  random_char3=random.choice(symbols)
  password.append(random_char3)
random.shuffle(password)
print(password)
p=""
for char in password:
  p=p+char
print(p)
#what's the difference b/w string and list?---- string and list both can be used for storing and loops can also be accessed in each of them but list can store all data types(char, int, float) but str can only store char. also nested lists are possible only in case of lists and not for strings. Many pre determined functions work with lists and not str. (eg.: random.shuffle())

PYTHON FUNCTIONS
1. Factorial
n=int(input("Enter a no.:"))
def factorial(n):
  S=1
  for i in range(1,n+1):
    S=S*i
  return S
print(factorial(n))

Ex.2 Build a function to calculate mean and median
def mean_median(n):
  n=int(input("Enter no. of observations:"))
  obs=[]
  for i in range(1,n+1):
    obs.append(int(input(f"enter {i}th observation:")))
  mean=sum(obs)/n
  obs.sort()
  if n%2==0:
    median=(obs[(n//2)]+obs[(n//2)+1])/2
  else:
    median=obs[(n//2)+1]
  print(f"mean={mean}")
  print(f"median={median}")
mean_median(5)
Ex.3 Build a function that calculates nPr
def permu(n,r):
  n=int(input("Enter n:"))
  r=int(input("Enter r:"))
  def factorial(n):
      S=1
      for i in range(1,n+1):
        S=S*i
      return S
  nPr=factorial(n)/factorial(n-r)
  print(nPr)
# permu(5,6)
Ex.4 Build a function to check whether a series is fibonacci or not.
def fibonacci(series):
  series=input("Enter series:").split(",")
  for i in range(1,len(series)+1):
    if series[i] == series[i - 1] + series[i - 2]:
      print("fibonacci")
      break
    else:
      print("not fibonacci")
      break
fibonacci(str)

Ex.5 Build a function to count vowels and consonants in a word.
def count(word):
    v=0
    c=0
    for i in word:
      if i in "aeiou":
        v=v+1
      else:
        c=c+1
    print(f"Vowels:{v}\nConsonants:{c}")
text=input("Enter the word:")
count(text)

Ex.6 WAP that asks user to enter a password. keep asking until all criteria are met.
criteria-- atleast one upper case, min. length 5, at least one digit.
print(type(2))
import string
letters = list(string.ascii_uppercase)
def validpassword(password):
    if len(password) < 5:
      print("Minimum 5 characters needed!")
    elif not any(char.isdigit() for char in password):
      print("At least one digit is needed!")
    elif not any(char.isupper() for char in password):
      print("At least one uppercase letter is needed!")
    else:
      print("Password is accepted.")
while True:
  p=input("Enter password:")
  validpassword(p)
  break
Ex.7 WAP that generates a random integer. ask the user to guess it. provide 5 hints at most until the user guesses correctly. Use a while loop to continue the game.

Ex.8 WAP that counts a specific character in a string.
def count(char,str):
  count=0
  for i in str:
    if i==char:
      count+=1
    else:
      count+=0
  print(count)
letter=input("enter the letter you want to count the no. of:")
text=input("enter the word/sentence/text:")
count(letter,text)

Ex.9 Use while loop to check a word is palindrome or not.
def palindrome(word):
  while word==word[::-1]:
    print("palindrome")
  else:
    print("not palindrome")
w=input("enter word:")
palindrome(w)

Mini Project:
1. Randomly choose a word from the word list and assign it to a variable named "chosen_word"
2. Ask the user to guess a letter and assign their answers to a variable called "guess". make the guess lowercase.
3. Check if the letter guessed by the user is one of the letters in the chosen word.

word_list = ['python', 'project', 'statistics', 'anjan sir', 'makaut']
import random

chosen_word = random.choice(word_list)
guess = input("guess a letter of the chosen word:")
if guess in chosen_word:
  print(f"{chosen_word} contains {guess}")
else:
  print(f"{chosen_word} doesn't contain {guess}")
#fibonacci series
str = input("Enter the series: ")


def is_fibonacci(series_str):
  # Split the input string into a list of numbers
  series = [int(num) for num in series_str.split(',')]

  if len(series) < 3:
    return False  # A Fibonacci sequence must have at least three numbers

  for i in range(2, len(series)):
    if series[i - 2] + series[i - 1] != series[i]:
      return False


#Example usage:
series1 = "0,1,1,2,3,5,8,13"
series2 = "1,2,3,6,9,15,24"

print(is_fibonacci(series1))  # True
print(is_fibonacci(series2))  # False

#CRYPTOGRAPHY APPLICATION: CEASER CYPHER

import string

letters = list(string.ascii_lowercase)


def encrypt(plain_text, shift_amount):
  cypher_text = ''
  for i in plain_text:
    position = letters.index(i)
    position = position + shift_amount
    new_word = letters[position]
    cypher_text = cypher_text + new_word
  return cypher_text


text = input("Enter the text:")
shift = int(input("Enter the cipher digit:"))
print(encrypt(text, shift))

#PYTHON DICTIONARIES
prog_dict = {
    "bug":
    "an error in a program that prevents the program from running as expected",
    "function": "an input-output structure to perform a certain task",
    "loop": "code which helps to do something repeatatively"
}
print(prog_dict["bug"])
prog_dict["Anjan"] = "takes python class"
print(prog_dict["Anjan"])
print(prog_dict)
# #dictionary takes character input values whereas list takes integer inputs

#looping
for i in prog_dict:
  print(i)  #prints only keys
  print(prog_dict[i])
#create an empty dictionary called student grades.
#write a code to insert grade to dictionary
#student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Jimmy": 99,
#     "Draco": 74,
#     "Snape": 62
# }
student_grades = {}
for i in range(1, 6):
  names = input("Enter name of student:")
  grades = input("Enter his grade:")
  student_grades[names] = grades
print(student_grades)
#NESTING
capitals = {"West Bengal": "Kolkata", "Bihar": "Patna"}
travel1 = {
    "WB": ["Kolkata", "Howrah", "Hooghly"],
    "Bihar": ["Patna", "Kisanganj"]
}
print(travel1["WB"][1])  #print Howrah
travel2 = {
    "WB": {
        "cities visited": ["Howrah", "Malda", "Jhargram"],
        "total visits": 3
    },
    "Bihar": {
        "cities visited": ["Patna", "Bhagalpur", "Mirzapur"],
        "total visits": 2
    }
}
print(travel2["WB"]["cities visited"][0])  #print Howrah
travel3 = [{
    "State": "WB",
    "cities visited": ["Howrah", "Malda", "Jhargram"],
    "total visits": 3
}, {
    "State": "Bihar",
    "cities visited": ["Patna", "Bhagalpur", "Mirzapur"],
    "total visits": 2
}]
print(travel3[0]["cities visited"][0])  #print Howrah

WB is a key under a dict travel2. WB is itself a dict with keys cities visited and total visits.
#keywords are always string but description can take values of any daatype.

Write a function that will add new state info in the travel list of dictionary
travel3 = [{
    "State": "WB",
    "cities visited": ["Howrah", "Malda", "Jhargram"],
    "total visits": 3
}, {
    "State": "Bihar",
    "cities visited": ["Patna", "Bhagalpur", "Mirzapur"],
    "total visits": 2
}]


def add_new(State, cities_visited, total_visits):
  dict = {}
  dict["State"] = State
  dict["cities_visited"] = cities_visited
  dict["total_visits"] = total_visits
  travel3.append(dict)
  print(travel3)


S = input("Enter name of the state:")
c = input("Enter the name of the cities visited:").split()
t = int(input("Enter number of times visited:"))
add_new(S, c, t)

#WAP which takes inputs of bidder info and amount of bidding and based on the amount of bidding, decide the winner.


def find_winner(total_players, bidder_info, amount):
  max_bid = amount[0]
  winner = bidder_info[0]
  for i in range(total_players):
    if amount[i] > max_bid:
      max_bid = amount[i]
      winner = bidder_info[i]
  return winner


t = int(input("Enter total number of players: "))
bidders = input("Enter names of bidders: ").split()
bids = [
    int(input(f"Enter the bid amount for {bidder}: ")) for bidder in bidders
]

winner = find_winner(t, bidders, bids)
print(f"The winner is {winner} with a bid of {max(bids)}")

#Build a scientific calculator that supports addition, subtraction, division, multiplication, sin ,cos and logarithmic values.

import math


def scientific_calculator():
  n = []

  def add():
    sum = 0
    for i in n:
      sum = sum + i
    return sum

  def subtract():
    diff = n[0]
    for i in n:
      diff = diff - i
    return diff

  def multiply():
    product = 1
    for i in n:
      product = product * i
    return product

  def divide():
    quotient = 1
    for i in n:
      quotient = quotient / i
    if n.index == 0:
      return "Cannot divide by zero."
    else:
      return quotient

  def sin(x):
    return math.sin(math.radians(x))

  def cos(x):
    return math.cos(math.radians(i))

  def log(x, base):
    return math.log(x, base)

  print("Scientific Calculator")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Sin")
  print("6. Cos")
  print("7. Logarithm")
  print("8. Exit")

  choice = input("Enter choice (1-8): ")

  if choice == '8':
    print("Exiting the calculator. Goodbye!")

  if choice in ('1', '2', '3', '4', '5', '6', '7'):
    if choice in ('1', '2', '3', '4', '7'):
      n = [float(y) for y in input("Enter the nos.: ").split()]
    else:
      x = float(input("Enter the number: "))

    if choice == '1':
      result = add()
      print(f"Result: {result}")
    elif choice == '2':
      result = subtract()
      print(f"Result: {result}")
    elif choice == '3':
      result = multiply()
      print(f"Result: {result}")
    elif choice == '4':
      result = divide()
      print(f"Result: {result}")
    elif choice == '5':
      result = sin(x)
      print(f"Sin({x}): {result}")
    elif choice == '6':
      result = cos(x)
      print(f"Cos({x}): {result}")
    elif choice == '7':
      base = float(input("Enter the base for logarithm: "))
      result = log(x, base)
      print(f"Log_{base}({x}): {result}")

  else:
    print("Invalid input. Please enter a number between 1 and 8.")


scientific_calculator()

