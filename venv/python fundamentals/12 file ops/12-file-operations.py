
word_frequencies = {}

with open("exercise12.txt", "r") as f:
    for line in f:
        line = line.strip()

        for word in line.split(' '):
            w_lower = word.lower().rstrip()
            word_frequencies[w_lower] = word_frequencies.get(w_lower, 0) + 1


print(word_frequencies)