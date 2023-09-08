# 1. Sum and multiplication of even and odd numbers.
# You are given an array of integers. Your task is to calculate two values: the sum of all even numbers and the product of all odd numbers in the array. Please return these two values as a list [sum_even, product_odd].
#
# Example
# For the array [1, 2, 3, 4]:

# def sum_even_and_product_odd(arr: list):
    # Initialize variables for the sum of even numbers and the product of odd numbers

arr = [1, 2, 3, 4]
sum_even = 0
product_odd = 1
n = len(arr)

for i in range(n):
    if arr[i] % 2 == 0:
        sum_even = sum_even + arr[i]
    else:
        product_odd = product_odd * arr[i]

print("Sum of even number is:", sum_even)
print("Product of odd number is:", product_odd)


# 2. Sum between range values
# You are given an array of integers and two integer values, min and max. Your task is to write a function that finds
# the sum of all elements in the array that fall within the range [min, max], inclusive.
#
# Example
# arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
# min_val = 3
# max_val = 7

def sum_elements_in_range(arr, min_val, max_val):
    total_sum = 0

    for num in arr:
        if min_val <= num <= max_val:
            total_sum += num

    return total_sum


num_list = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
min_num = 3
max_num = 7

result = sum_elements_in_range(num_list, min_num, max_num)
print(result)




# # 3. Stock price 2
# # You are given an array of prices where prices[i] is the price of a given stock on the ith day.
# # Find the maximum profit you can achieve.
# # You may complete as many transactions as you like (buy one and sell one share of the stock multiple times).
# #
# # Example: prices = [7, 1, 5, 3, 6, 4] Return: 7
#
def max_profit(prices: list, days: int) -> int:
    profit = 0

    for i in range(1, days):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit

prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices, len(prices))
print(profit)


# 4. Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the list to [1, 3, 0].

def plus_one(digits, n):
    digits.reverse()
    carry = 0

    for i in range(n):
        if (i == 0):
            digits[i] += (1 + carry)
        elif (carry != 0):
            digits[i] += carry

        carry = digits[i] // 10
        if (carry != 0):
            digits[i] = digits[i] % 10
    if (carry != 0):
        digits.append(carry)
    digits.reverse()


digits = [1, 2, 9]
n = len(digits)
plus_one(digits, n)

for i in digits:
    print(i, end=" ")

