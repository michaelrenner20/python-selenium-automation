# Level 1
# Question # 1. Reverse a negative integer and keep the negative sign at the beginning.
#
# Example: -189 -> -981


# def reverse_integer(n: int):
#    string = str(n)
#    if string[0] == '-':
#         return int( '-' + string[:0:-1])
#    else:
#         return int(string[::-1])
#
#
# print(reverse_integer(-189))
# print(reverse_integer(-981))


# Question # 2. Write a function that takes two strings as input and returns True if they are anagrams of each other, and False otherwise.
# The strings can contain uppercase and lowercase letters, and should be ignored during the comparison.
#
# Examples:
# Word 1: “race” Word 2: “care” should return “True”
# Word 1: “hEArt” Word 2: “earth” should return “True”
# Word 1: “rattle” Word 2: “battle” should return “False”


# def is_anagram(s1: str, s2: str):
#     s1 = s1.lower()
#     s2 = s2.lower()
#
#     if len(s1) != len(s2):
#         return False
#     if sorted(s1) == sorted(s2):
#         return True
#     else:
#         return False
#
#
# print(is_anagram("race", "care"))
# print(is_anagram("hEArt", "earth"))
# print(is_anagram("rattle", "battle"))


# Level 2
# # Question #3. Given a sentence, reverse the order of characters in each word.
# # “Hello World” should be transformed into “olleH dlroW”
# # “mistertwister” should be transformed into “retsiwtretsim”
#
# str1 = input("Enter the sentence")
# if str1:
#     words = str1.split()
#     rev_str1 = []
#     for i in words:
#     rev_str1.append(i[::-1])
#     sentence = " ".join(rev_str1)
#     print(sentence)
# else:
#     print("No input provided")



# Question 4. Given a string made of digits [0-9], return a string where each digit is
# repeated a number of times equals to its value.
# Examples:
# “312” should return “333122”
# “102” should return “122”

# def repeat_digits(s: str):
#   result = []
#
#   for char in s:
#         if char.isdigit():
#             repeat_count = int(char)
#             result.append(char * repeat_count)
#
#   return ''.join(result)
#
#
# print(repeat_digits("312"))
# print(repeat_digits("102"))


# Question # 5. Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u) in a given string.
# “y” is not considered a vowel for this task. The input string is always in lowercase.

def rem_vowel(string):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    return(result)

print(rem_vowel("hello"))
print(rem_vowel("goodbye"))
# # Time Complexity: O(n)