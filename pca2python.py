#!/usr/bin/env python
# coding: utf-8

# # Q1: Create a class representing a book with attributes like title, author, and publication year. Write methods to display the book details.

# In[1]:


class Book:
    def __init__(self,title,author,publication_year):
        self.title=title
        self.author=author
        self.publication_year=publication_year
        
    def frontpage(self):
        print(f"{self.title}\n By {self.author}\n DoubleDay Publishers \n")
        print(f"Revised Edition for year {self.publication_year}")       


# In[2]:


b=Book("The Girl on the Train","Paula Hawkins",2015)
b.frontpage()


# # Q2:Write a Python program using Turtle graphics to draw a square, a triangle, and a circle. 

# In[3]:


import turtle

#draw a square
def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

#draw a triangle
def draw_triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)

#draw a circle
def draw_circle():
    turtle.circle(50)

# Main function
def draw():
    turtle.speed(2)  # Set the drawing speed
    turtle.penup()
    turtle.goto(-150, 0)  # Move turtle to the starting position for square
    turtle.pendown()
    turtle.color("blue")
    draw_square()

    turtle.penup()
    turtle.goto(0, 0)  # Move turtle to the starting position for triangle
    turtle.pendown()
    turtle.color("red")
    draw_triangle()

    turtle.penup()
    turtle.goto(150, 0)  # Move turtle to the starting position for circle
    turtle.pendown()
    turtle.color("green")
    draw_circle()

    turtle.done()

if __name__ == "__main__":
    draw()


# # Q4: Generate a 5x5 NumPy array where each element is a random integer between 10 and 50 (inclusive), and none of the elements are repeated.

# In[4]:


import numpy as np


# In[5]:


arr=np.random.randint(10,51,size=(5,5))


# In[6]:


print(arr)


# # Q5: Create a Turtle graphics program that generates and visualizes a random maze. Use different colors for walls and paths.

# In[5]:


import turtle
import random

# Function to draw a rectangle with given coordinates, width, and height
def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Function to draw the maze
def draw_maze(rows, columns, cell_width, cell_height):
    for i in range(rows):
        for j in range(columns):
            x = j * cell_width - (columns * cell_width) / 2
            y = -i * cell_height + (rows * cell_height) / 2
            if random.random() < 0.3:  # Probability of creating a wall
                draw_rectangle(x, y, cell_width, cell_height, "black")
            else:
                draw_rectangle(x, y, cell_width, cell_height, "white")

# Main function
def main():
    turtle.tracer(0)  # Turn off animation
    turtle.hideturtle()  # Hide the turtle
    turtle.bgcolor("white")  # Set the background color

    rows = 20
    columns = 20
    cell_width = 20
    cell_height = 20

    draw_maze(rows, columns, cell_width, cell_height)

    turtle.update()  # Update the screen once all drawing is complete
    turtle.done()

if __name__ == "__main__":
    main()


# In[ ]:




