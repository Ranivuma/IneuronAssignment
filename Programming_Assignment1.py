#1. Write a Python program to print &quot;Hello Python&quot;?
def greet():
    print("Hello Python")
greet()

#2. Write a Python program to do arithmetical operations addition and division.?

def add(a,b):
    return a+b
def div(a,b):
    return a/b
add(3,4)
div(4,2)

#3. Write a Python program to find the area of a triangle?
# formula = 1/2 * b* h
b=int(input("Enter the base of a triangle"))
h =int(input("Enter the height of a triangle"))
def area_triangle():
    return 1/2 * b* h
print(area_triangle())

#4. Write a Python program to swap two variables?
a=5
b=0
print("Before swapping")
print("a value is ", a)
print("b value is ", b)
a,b= b,a
print("After swapping")
print("a value is ", a)
print("b value is ", b)

#5. Write a Python program to generate a random number?

import random
n = random.random()
print(n)