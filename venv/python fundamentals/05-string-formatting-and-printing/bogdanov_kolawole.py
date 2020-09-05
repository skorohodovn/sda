"""
Write a Python program to reverse a string if its length is a multiple of 4. Print the result.
Example:
reverse_if_d4.py some_string_here
ereh_gnirts_emos
reverse_if_d4.py not_multiple_of_4
not_multiple_of_4
"""

import sys
str = sys.argv
length = len(str)

if length%4 == 0:
    print(str[::-1])
else:
    print("Not 4 char long!")