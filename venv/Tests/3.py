import re
sum = 0
pattern = 'back'
if re.match(pattern, 'backup.txt'):
    sum += 1
if re.match(pattern, 'text.back'):
    sum += 2
if re.search(pattern, 'backup.txt'):
    sum += 4
if re.search(pattern, 'text.back'):
    sum += 8

print(sum)