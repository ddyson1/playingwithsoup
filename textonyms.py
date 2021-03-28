import nltk, re, pprint
from nltk import word_tokenize

wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

"""
1[   ]  2[abc]  3[def]
4[ghi]  5[jkl]  6[mno]
7[pqrs] 8[tuv]  9[wxyz]
"""

print([w for w in wordlist if re.search('^[def][tuv][abc][jkl]$', w)])
