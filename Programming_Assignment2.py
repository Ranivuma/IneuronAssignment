
#1. Write a Python program to convert kilometers to miles?
# formula to convert kilometers to miles is 1 kilometer (km) = 0.62137 miles (mi)
kilometer =float(input("Enter the Value in kilo meter to convert into miles"))
def convert(kilometer):
    return kilometer * 0.62137
miles = convert(kilometer)
print("The miles for the ",kilometer," kilometer is",miles)


#2. Write a Python program to convert Celsius to Fahrenheit?
# formula Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.

celsius  = float(input("Enter the Celsius to know the equivalent Fahrenheit"))

Fahrenheit = celsius * 1.8 +32
print("The Fahrenheit for the ", celsius,'celsius is ',Fahrenheit)

#3. Write a Python program to display calendar?
import calendar
yy = int(input("Enter the year in four digit"))
# display the calendar
print(calendar.calendar(yy))

#4. The following program is used to find out the roots of the quadratic equation

import math
def equationroots(x, y, z):
    discri = y * y - 4 * x * z


sqrtval = math.sqrt(abs(discri))

# checking condition for discriminant

if discri > 0:
    print(" real and different roots ")
    print((-y + sqrtval) / (2 * x))
    print((-y - sqrtval) / (2 * x))
elif discri == 0:
    print(" real and same roots")
    print(-y / (2 * x))
else:
    print("Complex Roots")
    print(- y / (2 * x), " + i", sqrt_val)
    print(- y / (2 * x), " - i", sqrt_val)
# Driver Program
x = 1
y = 10
z = -24
if x == 0:
    print("Input correct quadratic equation")
else:

    equationroots(x, y, z)

#Write a Python program to swap two variables?
a=5
b=0
print("Before swapping")
print("a value is ", a)
print("b value is ", b)
a,b= b,a
print("After swapping")
print("a value is ", a)
print("b value is ", b)
