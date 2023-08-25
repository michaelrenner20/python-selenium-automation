# #LEVEL 1
# # Question 1
# def bin_go(n: int):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 7 == 0:
#             print(f'{i} : BinGo')
#         elif i % 3 == 0:
#             print(f'{i} : Bin')
#         elif i % 7 == 0:
#             print(f'{i} : Go')
#         else:
#             print(i)
#
#
# #bin_go(n=100)
#
# # Question 2
# def sum_numbers(n: int):
#     result = 1
#     for i in range (0, n+1):
#         result = result + i
#     print(f"The sum of {n} is {result}")
#
# sum_numbers(10)
#
# #LEVEL 2
# # Question 1
# def find_max(a: int, b: int, c: int):
#     #list = [a, b, c]
#     print("Maximum Number is: ", max(a, b, c))
#     if a > b and a > c:
#         max_num = a
#     elif b > a and b > c:
#         max_num = b
#     else:
#         max_num = c
#     return max_num
#
# x = int(input("Enter First number: "))
# y = int(input("Enter Second number: "))
# z = int(input("Enter Third number: "))
#
# print(find_max(a=x, b=y, c=z))
#
#
#
# # Question 2
#
# def leap_year(year):
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100!= 0):
#         print("It is a leap year")
#     else:
#         print("It is not a leap year")
#
# #input_year = int(input("Enter a year:"))
# #leap_year(input_year)
#
# # LEVEL 3
# # Question 1
# def fibonacci_sequence(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input entered")
#     elif n == 0:
#         print(a)
#     elif n == 1:
#         print(b)
#     else:
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#             print(b)
# fibonacci_sequence(9)


#0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
# O(n) time complexity

# # Algorithms Lesson 2
# #Built in functions
# string = "This is the \"text\" of the string"
# print("is" in string)
# print("if" in string)
# print(string[0]) # access T or first letter of the string
# print (string[:4]) #access first 4 characters
# print(string[0:10:2])
# print(string + " plus something extra") #combine strings (concatenation)
# print(len(string)) #length of string
# print(string.lower()) #lowercase
# print(string.upper()) #uppercase
# print(string.split()) # split into seperate words
# list_of_strings = string.split("t")
# print(list_of_strings)
# print("+".join(list_of_strings))#joining strings
# print(string.strip()) #eliminates spaces in front or after a string but not within the string
# print(string.replace()) #replace characters with a different character
# print(string.find("i")) #finds the index or gives -1 if it's not in the string
# def reverse_string(s: str):
#     print[::-1] to reverse a string

# def is_anagram(s1: str, s2: str):
#     if len(s1) !=len(s2):
#         return False
#     if sorted(s1) == sorted(s2):
#         return True
#     else:
#         return False
#
# print(is_anagram(s1: 'cat', s2: 'act'))
# print(is_anagram(s1: "cat", s2: "ace"))

# def is_palindrome(s: str):
#
#     if (s == s[::-1]):
#         return("The string is a palindrome")
#     else:
#         return("The string is not a palindrome")
#
# print(is_palindrome('rabbit'))



def is_almost_palindrome(s: str):
    word = len(s)
    for i in range(word):
       new_s = s[:i] + s[i+1:]
       if new_s == new_s[::-1]:
            return True

    return False
