john = open("bookofjohn.txt", "r")


key_words = ["Father", "God", "Christ", "Spirit", "spirit", "life", "man"]

john_freq = {}

for k in key_words:
    john_freq[k] = 0


for word in john:
    for w in word.split():
        if w in john_freq:
            john_freq[w] += 1


for key, value in john_freq.items():
    print(key, ": ", value, sep="")
