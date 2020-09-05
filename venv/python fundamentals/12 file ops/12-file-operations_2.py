import os
word_frequencies = {}
total_word_no = 0

with open("exercise123.txt", "r") as f:
    for line in f:
        line = line.strip()

        for word in line.split(' '):
            w_lower = word.lower().rstrip()
            word_frequencies[w_lower] = word_frequencies.get(w_lower, 0) + 1
            total_word_no += 1


print(word_frequencies)
print(total_word_no)

frequencies_str = str(word_frequencies)
total_word_str = str(total_word_no)

with open('outputfile.txt','w') as of:
    of.write(total_word_str )
    of.write(frequencies_str)

with open('outputfile2.txt','w') as of:
    print(total_word_no, file = of)
    print(word_frequencies, file = of)