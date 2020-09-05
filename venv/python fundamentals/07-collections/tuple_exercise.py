import sys

recipe = ('boil water', 'insert egg', 'wait 5min', 'eat')

print(len(recipe))
print(recipe[2])
print(recipe[len(recipe)-2:len(recipe)])
print(recipe[-2:])


if recipe.index('boil water') == 0:
    print(f"boil water is first step")