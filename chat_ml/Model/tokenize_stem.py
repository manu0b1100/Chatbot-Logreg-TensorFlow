import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
stopwords=set(stopwords.words('english'))
stopwords.add(',')
stopwords.add('.')
stopwords.add('sopra')
stopwords.add('steria')
def stem_tokens(tokens):
    stemmer = PorterStemmer()
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    tokens = [w for w in tokens if w not in stopwords]
    tokens = stem_tokens(tokens)
    return ' '.join(tokens)



def clean(text):
    text = text.lower()
    text = tokenize(text)
    return text