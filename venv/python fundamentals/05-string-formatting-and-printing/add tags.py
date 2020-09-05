# Write a Python program to create the HTML string with tags around the word(s).
# Example:
"""
add_tags.py i Python
<i>Python</i>
add_tags.py b "Python Tutorial"
<b>Python Tutorial </b>
"""
import sys

_, tag, string = sys.argv

print(f"<{tag}>{string}</{tag}>")


