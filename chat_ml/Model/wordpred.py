import pandas as pd

newtable=pd.read_csv("./chat_ml/Data/ngram.csv")
def getResultList(word):
    unigram=word.split()[-1]
    bigram=word
    mylist=newtable[(newtable.ngram==bigram)].sort_values('freq',ascending=False)['nextword'].append(newtable[(newtable.ngram==unigram)].sort_values('freq',ascending=False)['nextword'])
    return mylist.unique().tolist()