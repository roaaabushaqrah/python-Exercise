# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
# for x in range(1500, 2700):
#     if(x % 7 == 0) and (x % 5 == 0):
#         print(x)
# Write a Python program to convert temperatures to and from celsius, fahrenheit.
# celsius = float(input("Enter the temperature in celcius:"))
# f = (celsius*1.8)+32
# print("Temperature in farenheit is:", f)
# Write a Python program to construct the following pattern, using a nested for loo

# for i in range(1, 5):
#     for j in range(1, 5):
#         if j <= i:
#             print("*", end="")
#         else:
#     print("")

#     print()

# for i in range(n, 0, -1):
#     for j in range(i):
#         print('* ', end="")
#     print('')
# Write a Python program to count the number of even and odd numbers from a series of numbers
# import re
# NUM = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # Declaring the tuple
# count_odd = 0
# count_even = 0
# for x in NUM:
#     if not x % 2:
#         count_even += 1
#     else:
#         count_odd += 1
# print("Number of even numbers :", count_even)
# print("Number of odd numbers :", count_odd)
# # Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
# for x in range(6):
#     if (x == 3 or x == 6):
#         continue
#     print(x, end=' ')
# print("\n")
# # Write a Python program to get the Fibonacci series between 0 to 50.
# x, y = 0, 1

# while y < 50:
#     print(y)
#     x, y = y, x+y
# # Write a Python program that accepts a string and calculate the number of digits and letters.
# s = input("Input a string")
# d = l = 0
# for c in s:
#     if c.isdigit():
#         d = d+1
#     elif c.isalpha():
#         l = l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)

# Write a Python program to check the validity of password input by users. Validation
# p = input("Input your password")
# x = True
# while x:
#     if (len(p) < 6 or len(p) > 12):
#         break
#     elif not re.search("[a-z]", p):
#         break
#     elif not re.search("[0-9]", p):
#         break
#     elif not re.search("[A-Z]", p):
#         break
#     elif not re.search("[$#@]", p):
#         break
#     elif re.search("\s", p):
#         break
#     else:
#         print("Valid Password")
#         x = False
#         break

# if x:
#     print("Not a Valid Password")
# # Write a Python program to calculate a dog's age in dog's years.
# age = int(input("Input a dog's age in human years: "))

# if age < 0:
#     print("Age must be positive number.")
#     exit()
# elif age <= 2:
#     age2 = age * 10.5
# else:
#     age2 = 21 + (age - 2)*4

# print("The dog's age in dog's years is", age2)
# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20def sum(x, y):
#   sum = d + f
#    if sum in range(15, 20):
#         return 20
#     else:
#         return sum

# print(sum(10, 6))
# print(sum(10, 2))
# print(sum(10, 12))

# num1 = float(input("Input first number: "))
# num2 = float(input("Input second number: "))
# num3 = float(input("Input third number: "))
# if num1 > num2:
#     if num1 < num3:
#         median = num1
#     elif b > num3:
#         median = num2
#     else:
#         median = num3
# else:
#     if num1 > num3:
#         median = num1
#     elif num2 < num3:
#         median = num2
#     else:
#         median = num3
# Write a Python program to find the median of three values
# print("The median is", median)
