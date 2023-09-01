# list_words = ['apple', 'kiwi', 'banana', 'orange']
# list_numbers = [3, 4, 2, 1]
#
# print(list_words)
# print(list_numbers.insert(3, 99)) # if you want to insert 99 @ index 3

arr1_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2_list = [1, 3, 2, 4, 6, 5, 8, 9]
for i in arr1_list:
    if i in arr2_list:
        print("in both lists", i)
    else:
        print("missing", i)

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

def isMountainArray(arr: list):
    i = 1
    while i < len(arr) and arr[i - 1] < arr[i]:
        i += 1

    if i == 1 or i == len(arr):
        return False

    while i < len(arr) and arr[i - 1] > arr[i]:
        print(i)
        i += 1

    if i == len(arr):
        return True
    else:
        return False






