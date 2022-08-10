#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Write a Python Program to Find LCM?
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1=min1+1


# In[2]:


#2. Write a Python Program to Find HCF?
num1 = 36
num2 = 60
hcf = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("Hcf of", num1, "and", num2, "is", hcf)


# In[3]:


#3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
dec = int(input("Enter an integer: "))
print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")


# In[4]:


#4. Write a Python Program To Find ASCII value of a character?
c = 'g'
# print the ASCII value of assigned character in c
print("The ASCII value of '" + c + "' is", ord(c))


# In[5]:


#5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical
def add(P, Q):    
 
   return P + Q   
def subtract(P, Q):   
  
   return P - Q   
def multiply(P, Q):   
   
   return P * Q   
def divide(P, Q):   
    
   return P / Q    
 
print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")    
    
choice = input("Please enter choice (a/ b/ c/ d): ")    
    
num_1 = int (input ("Please enter the first number: "))    
num_2 = int (input ("Please enter the second number: "))    
    
if choice == 'a':    
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
elif choice == 'b':    
   print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
    
elif choice == 'c':    
   print (num1, " * ", num2, " = ", multiply(num1, num2))    
elif choice == 'd':    
   print (num_1, " / ", num_2, " = ", divide(num_1, num_2))    
else:    
   print ("This is an invalid input")    

