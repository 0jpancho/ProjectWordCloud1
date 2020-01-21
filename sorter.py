import operator

file = open("pandp.txt", "r", encoding = "utf8")

words = {}

for word in file.read().split():
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

sortedWords = sorted(words.items(), key = operator.itemgetter(1), reverse = True)
print(sortedWords)
