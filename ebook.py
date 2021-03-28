import nltk, re, pprint
from nltk import word_tokenize
from urllib import request

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

print(type(raw))
print(len(raw))
print(raw[:75])

tokens = word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:10])

text = nltk.Text(tokens)
print(type(text))
print(text[1024:1062])
print(text.collocations())

beginning = raw.find("PART I")
end = raw.rfind("End of Project Gutenberg's Crime")
raw = raw[beginning:end]

print(raw)
