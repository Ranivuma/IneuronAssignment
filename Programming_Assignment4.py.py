#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Write a Python Program to Find the Factorial of a Number?

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
num = 5;
print("Factorial of",num,"is",
factorial(num))


# In[2]:


#2. Write a Python Program to Display the multiplication Table?
number = int(input("Enter the number to get the multiplication table"))
for i in range(1,11,1):
    print(number,'X',i,'=',i*number)


# In[5]:


#3. Write a Python Program to Print the Fibonacci sequence?
n=10
first,second =0,1
for i in range(n):
    third = first+second
    print(third)
    first,second =second,third
    


# In[13]:


#4.Write a Python Program to Check Armstrong Number?
n = int(input("Enter a number: "))
#initialize the sum
s = 0
t = n
while t > 0:
   digit = t % 10
   s += digit ** 3
   t //= 10
# display the result
if n == s:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")


# In[14]:


#5. Write a Python Program to Find Armstrong Number in an Interval?
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
 
for num in range(lower,upper + 1):
   # initialize sum
   sum = 0
 
   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num)


# In[15]:


#6. Write a Python Program to Find the Sum of Natural Numbers?
n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)

