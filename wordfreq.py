wordfreq = dict()
with open("common-words.txt") as f:
    for i, word in enumerate(f.readlines()):
        wordfreq[word.strip()] = i
