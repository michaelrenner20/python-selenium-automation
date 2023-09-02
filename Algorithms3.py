# CLASSROOM INFO/EXAMPLES:
# list_words = ['apple', 'kiwi', 'banana', 'orange']
# list_numbers = [3, 4, 2, 1]
#
# print(list_words)
# print(list_numbers.insert(3, 99)) # if you want to insert 99 @ index 3

# arr1_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr2_list = [1, 3, 2, 4, 6, 5, 8, 9]
# for i in arr1_list:
#     if i in arr2_list:
#         print("in both lists", i)
#     else:
#         print("missing", i)

# def find_missing_element(arr1: list, arr2: list):
# arr1_list.sort()
# arr2_list.sort()
#
# for i in range(len(arr2_list) -1):
#     if arr1_list[i] != arr2_list[i]:
#         print(str(arr1_list[i]) + 'is the missing element')
#             return
#     print('The end of function')
#     print(str(arr1_list[-1]) + 'is the missing element')
#
# testarr1_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# testarr2_list = [1, 3, 2, 4, 6, 5, 8, 9]
# find_missing_element(testarr1_list, testarr2_list)

# def largest_cont_sum(arr: list):
#     cur_sum = max_sum = arr[0]
#
#     for num in arr[1]:
#         cur_sum = max(cur_sum + num, num)
#         max_sum = max(max_sum, cur_sum)
#
#     return max_sum
#
# test_list = [-4, 2, ] # still need to complete test list

# def isMountainArray(arr: list):
#     i = 1
#     while i < len(arr) and arr[i - 1] < arr[i]:
#         i += 1
#
#     if i == 1 or i == len(arr):
#         return False
#
#     while i < len(arr) and arr[i - 1] > arr[i]:
#         print(i)
#         i += 1
#
#     if i == len(arr):
#         return True
#     else:
#         return False



# HOMEWORK
# Task 1. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
#
#
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
# def find_two_lowest(arr: list):

num_arr = [198, 3, 4, 9, 10, 9, 2, 0, -1, 20]
num_arr.sort()
print(num_arr)
print(num_arr[0])
print(num_arr[1])



# Task 2
# Given a list of numbers, return the inverse of each. Each positive
# becomes a negative, and the negatives become positives.
#
# Example:
# Input: [1, 5, -2, 4]
# Output: [-1, -5, 2, -4]
# Loop through each index of the array
def invert(lst):
    return [-i for i in lst]

lst = [1, 5, -2, 4]
print(invert(lst))



# Task 3
# Implement a function that returns the difference between the largest and the smallest value in a given list.
# The list contains positive and negative numbers. All elements are unique.

num_arr = [3, 5, 7, 2, 1, 9, 20, -4, -1]
num_arr.sort()
print(num_arr)
print(num_arr[-1] - num_arr[0])



# Task 4
# Write a function that counts the number of elements in a given list larger than their adjacent neighbors.
#
# Example:
# Input: [2, 56, 7, 21, 22, 19, 26]
# Output: 3 (56, 22)

# my code, not quite correct and not sure why?
# def count_larger_neighbors(arr):
#     num = 0
#     for i in range(len(arr)):
#         if i == 0: and arr[i] > arr[i + 1]:
#             num += 1
#         elif i == len(arr) - 1 and arr[i] > arr[i-1]:
#             num += 1
#         elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
#             num += 1
#
#     return num
# lst = [2, 56, 7, 21, 22, 19, 26]
# result = (count_larger_neighbors(lst))
# print(result)

# my code that is correct with some help
def count_elements_larger_than_neighbors(arr):
    count = 0
    for i in range(len(arr)):
        if i == 0 and arr[i] > arr[i + 1]:
            count += 1
        elif i == len(arr) - 1 and arr[i] > arr[i - 1]:
            count += 1
        elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1

    return count


input_list = [2, 56, 7, 21, 22, 19, 26]
result = count_elements_larger_than_neighbors(input_list)
print(result)



# Task 5
# Given an array. Find the minimum element in the list and subtract it from each element in the array.
#
# Example:
# Input: [9, 2, 5, 4, 7, 6, 1]
# The minimum element in the list: 1
# Output: [8, 1, 4, 3, 6, 5, 0]

def subtract_min(arr: list):
    min_element = min(arr)
    new_list = []
    for elem in arr:
        new_list.append(elem - min_element)

    return new_list


num_arr1 = [9, 2, 5, 4, 7, 6, 1]
print(subtract_min(num_arr1))

