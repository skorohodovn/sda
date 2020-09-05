"""
Write a Python program to get a string made of 4
copies of the last two characters of a specified string (length must be at least 2).
Example:
insert_end.py Python
onononon
insert_end.py Exercises
eseseses
"""
import sys
str = sys.argv
length =len(str)

print(str[length-2:length]*4)
