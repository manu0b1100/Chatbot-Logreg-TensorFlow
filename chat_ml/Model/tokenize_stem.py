import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
stopwords1=set(stopwords.words('english'))
stopwords1.add(',')
stopwords1.add('.')
stopwords1.add('sopra')
stopwords1.add('steria')
stopwords1.remove('when')
stopwords1.remove('who')
stopwords1.remove('where')
stopwords1.remove('about')
stopwords1.remove('do')

stopwords2=set(stopwords.words('english'))
stopwords2.add(',')
stopwords2.add('.')
stopwords2.remove('do')

stopwords2.remove('when')
stopwords2.remove('who')
stopwords2.remove('where')
stopwords2.remove('about')

def stem_tokens(tokens):
    stemmer = PorterStemmer()
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def tokenize(text):
    tokens1 = nltk.word_tokenize(text)
    tokens1 = [w for w in tokens1 if w not in stopwords1]
    tokens2 = nltk.word_tokenize(text)
    tokens2 = [w for w in tokens2 if w not in stopwords2]
    if len(tokens1)==0 and len(tokens2) != 0:
        tokens1=tokens2
    tokens = stem_tokens(tokens1)
    return ' '.join(tokens)



def clean(text):
    text = text.lower()
    text = tokenize(text)
    return text

def cleanAndMerge(ques):
    corpus=[]
    for i in range(0,ques.size):
        text=ques[i]
        text=clean(text)
        corpus.append(text)
    return corpus
