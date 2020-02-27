""" Script to determine the frequency count of words in a file """

freq = {}
for piece in open("test.txt").read().lower().split():
    word = "".join(c for c in piece if c.isalpha())
    if word:
        freq[word] = 1 + freq.get(word, 0)
        # print(freq)

max_word = ''
max_count = 0
for (w, c) in freq.items():
    if c > max_count:
        max_word = w
        max_count = c

print("The most frequent word is {0}".format(max_word))
print("Its ocurrence count is {}".format(max_count))