import os

print(f"PYTHONPATH value: {os.getenv('PYTHONPATH')}")
print("Trying to import examplepackage")
import examplepackage

print("Success!")
