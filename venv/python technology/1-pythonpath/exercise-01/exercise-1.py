# q2
# from examplepackage.symbols import happy_symbol
# print(happy_symbol)

#q3
from examplepackage.symbols import *
x = all(x in globals() for x in ["happy_symbol", "sad_symbol", "confused_symbol", "all_symbols"])
print(x)
print(all_symbols)

#q4

import examplepackage
y = all(examplepackage.functions.is_symbol(s) for s in all_symbols)
print(y)

