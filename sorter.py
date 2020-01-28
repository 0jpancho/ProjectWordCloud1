from wordcloud import WordCloud

import matplotlib.pyplot as plt
# % matplotlib inline
# c:\intelpython3\lib\site-packages\matplotlib\__init__.py:
import warnings

warnings.filterwarnings("ignore")

file = open("pandp.txt", "r", encoding="utf8")

words = {}

for word in file.read().split():
    if word not in words:
        for i in word:
            if "'" or '"' or ';' or ':' or ',' or '.' in i:
                i.replace(i, " ", 1)
            else:
                pass
        words[word] = 1
    else:
        words[word] += 1

delWords = ['the', 'to', 'of', 'and', 'a', 'her', 'in', 'was', 'I', 'that', 'not', 'she', 'be', 'his', 'had', 'as', 'with', 'he', 'for', 'you', 'it', 'have', 'is', 'Mr.', 'at', 'on', 'by', 'but', 'my', 'were', 'all', 'so',
            'which', 'been', 'him', 'could', 'from', 'they', 'very', 'would', 'no', 'their', 'your', 'will', 'what', 'such', 'this', 'or', 'an', 'said', 'Mrs.', 'are', 'must', 'am', 'She', '"I', 'any', 'more', 'much', 'than',
            'when', 'The', 'Miss', 'do', 'them' 'me', 'who', 'there', 'if', 'should', 'But', 'one', 'did', 'Darcy', 'has', 'He', 'never', 'only', 'It', 'some', 'soon', 'though', 'can', 'might', 'we', 'may', 'know', 'think',
            'every', 'most', 'being', 'other', 'Bennet', 'little', 'make', 'before', 'how', 'after', 'now', 'shall']
for i in delWords:
    if i in words:
        del words[i]



sortedWords = dict(sorted(words.items(), key=lambda x: x[1], reverse=True))
print(sortedWords)
wc = WordCloud(normalize_plurals=False).generate_from_frequencies(sortedWords)
plt.imshow(wc)
plt.show()
