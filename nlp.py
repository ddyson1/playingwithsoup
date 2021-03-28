import nltk
import nltk.data
from nltk.text import Text
from nltk import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus import wordnet as wn
# from nltk.book import *

# nltk.download()
# nltk.download('gutenberg')

# text1.concordance("water")
# print(FreqDist(text1).most_common(50))
# FreqDist(text1).plot(50, cumulative=True)
# print(set(text1))

corpus_root = '/Users/devindyson/Desktop/beautifulsoup/corpora'
corpora = PlaintextCorpusReader(corpus_root, '.*')

# print(corpora.raw('meditations.txt'))
# print(SentimentIntensityAnalyzer().polarity_scores("NLTK is pretty dope."))

print(sorted(corpora.fileids()))
print(len(corpora.words('meditations.txt')))
print(len(corpora.words('benjamin.txt')))

meditations = Text(corpora.words('meditations.txt'))
benjamin = Text(corpora.words('benjamin.txt'))

def lexical_diversity(text_data):
    word_count = len(text_data)
    vocab_size = len(set(text_data))
    diversity_score = vocab_size / word_count
    return diversity_score

print(lexical_diversity(meditations))
print(lexical_diversity(benjamin))
# print(FreqDist('meditations.txt').most_common(50))

# print(meditations.concordance("virtue"))

# print(FreqDist(meditations).most_common(50))
# FreqDist(meditations).plot(50, cumulative=True)

print(wn.synsets('virtue'))

print(wn.synset('virtue.n.01').lemma_names())
print(wn.synset('virtue.n.01').definition())
print(wn.synset('virtue.n.01').examples())
