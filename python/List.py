# 1. Write a Python program to sum all the items in a list.
# def sum_list(items):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#     return sum_numbers


# print(sum_list([10, 2, 8]))

# 2. Write a Python program to multiply all the items in a list
# def multiplyList(myList):

#     # Multiply elements one by one
#     result = 1
#     for x in myList:
#         result = result * x
#     return result


# # Driver code
# list1 = [10, 21, 13]
# list2 = [3, 2, 4]
# print(multiplyList(list1))
# print(multiplyList(list2))
# 3. Write a Python program to get the largest number from a list.
# list1 = [10, 20, 4, 45, 99]

# # sorting the list
# list1.sort()

# # printing the last element
# print("Largest element is:", list1[-1])
# Write a Python program to get the smallest number from a list
# a = [18, 52, 23, 41, 32]

# # find smallest number using min() function
# smallest = min(a)

# # print the smallest number
# print(f'Smallest number in the list is : {smallest}.')
# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are the same from a given list of strings
# def match_words(words):
#     ctr = 0

#     for word in words:
#         if len(word) > 1 and word[0] == word[-1]:
#             ctr += 1
#     return ctr


# print(match_words(['abc', 'xyz', 'aba', '1221']))

# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# def last(n): return n[-1]


# def sort_list_last(tuples):
#     return sorted(tuples, key=last)

# Write a Python program to remove duplicates from a list.
# def Remove(duplicate):
#     final_list = []
#     for num in duplicate:
#         if num not in final_list:
#             final_list.append(num)
#     return final_list


# # Driver Code
# duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
# print(Remove(duplicate))


# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
# Write a Python program to check if a list is empty or not.
# l = []
# if not l:
#     print("List is empty")
# Write a Python program to clone or copy a list
# original_list = [1, 2, 4, 22, 4]
# new_list = list(original_list)
# print(original_list)
# print(new_list)
# Write a Python program to find the list of words that are longer than n from a given list of words
# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len


# print(long_words(3, "Coding Academy by orange"))
# Write a Python function that takes two lists and returns True if they have at least one common member
# def common_data(list1, list2):
#     result = False
#     for x in list1:
#         for y in list2:
#             if x == y:
#                 result = True
#                 return result


# print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
# print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]
# print(color)
# Write a Python program to generate a 3*4*6 3D array whose each element is
# array = [[['Roaa' for col in range(6)]
#           for col in range(4)] for row in range(3)]
# print(array)
# Write a Python program to print the numbers of a specified list after removingeven numbers from it
# num = [71, 18, 20, 5, 41, 55, 27]
# num = [x for x in num if x % 2 != 0]
# print(num)
# Write a Python program to shuffle and print a specified list.
# from random import shuffle
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(color)
# print(color)
# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
# def printValues():
#     l = list()
#     for i in range(1, 21):
#         l.append(i**2)
#     print(l[:5])
#     print(l[-5:])


# printValues()
# Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
# def printValues():
#     l = list()
#     for i in range(1, 31):
#         l.append(i**2)
#     print(l[5:])
# Write a Python program to generate all permutations of a list in Python
# import itertools
# print(list(itertools.permutations([1, 2, 3])))
# Write a Python program to get the difference between the two lists
# list1 = [1, 3, 5, 7, 9]
# list2 = [1, 2, 4, 6, 7, 8]
# diff_list1_list2 = list(set(list1) - set(list2))
# diff_list2_list1 = list(set(list2) - set(list1))
# total_diff = diff_list1_list2 + diff_list2_list1
# print(total_diff)
# Write a Python program to access the index of a list
# nums = [5, 15, 35, 8, 98]
# for num_index, num_val in enumerate(nums):
#     print(num_index, num_val)
