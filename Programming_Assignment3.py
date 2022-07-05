#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

number = int(input("Enter a number to check it is +ve, -ve, Zero"))
if number == 0:
    print("The number is Zero")
elif number >= 1:
    print("The number is Positive")
elif number <= 1:
    print("The number is negative")
#2. Write a Python Program to Check if a Number is Odd or Even?

def check(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
number = int(input("Enter the number to check odd r Even"))
check(number)

#3. Write a Python Program to Check Leap Year?
year = int(input("Enter the year in 4 digit to check whether it is leap year or not"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("True")
        else:
            print("False")
    else:
        print("True")
else:
    print("False")


#4. Write a Python Program to Check Prime Number?
# Python program to check if
# given number is prime or not

num = int(input("Enter a number to check whether it is prime number or not"))

# If given number is greater than 1
if num > 1:

  # Iterate from 2 to n / 2
  for i in range(2, int(num/2)+1):

    # If num is divisible by any number between
    # 2 and n / 2, it is not prime
    if (num % i) == 0:
      print(num, "is not a prime number")
      break
  else:
    print(num, "is a prime number")

else:
  print(num, "is not a prime number")

#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


def prime(x, y):
  prime_list = []
  for i in range(x, y):
    if i == 0 or i == 1:
      continue
    else:
      for j in range(2, int(i/2)+1):
        if i % j == 0:
          break
      else:
        prime_list.append(i)
  return prime_list

# Driver program
starting_range = 1
ending_range = 10000
lst = prime(starting_range, ending_range)
if len(lst) == 0:
  print("There are no prime numbers in this range")
else:
  print("The prime numbers in this range are: ", lst)
