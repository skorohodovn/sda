import os

filename = os.path.join('12 file ops', 'example_script.py')

print(filename)

with open(filename, 'w') as f:
    f.write('print("Hello, world")')

