import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup

url = 'https://news.mit.edu/2021/filters-sapwood-purify-water-0325'
html = request.urlopen(url).read().decode('utf8')

raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = word_tokenize(raw)
text = nltk.Text(tokens)

text.concordance('MIT')

"""
def freq_words(url, freqdist, n):
    html = request.urlopen(url).read().decode('utf8')
    raw = BeautifulSoup(html, 'html.parser').get_text()
    for word in word_tokenize(raw):
        freqdist[word.lower()] += 1
    result = []
    for word, count in freqdist.most_common(n):
        result = result + [word]
    print(result)
"""
