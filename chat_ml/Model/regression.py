import pandas as pd
from sklearn.externals import joblib
from .tokenize_stem import clean
from chat_ml.Analytics.pushToDatabase import *

class Lregression:
    def __init__(self):
        # print("initialised")
        self.chatdata = pd.read_csv("./chat_ml/Data/processedchatdata.csv",converters={'corpus':str})
        self.le = joblib.load('./chat_ml/Data/lencoder.pkl')
        self.logreg = joblib.load('./chat_ml/Data/logistic.pkl')
        self.tfidf = joblib.load('./chat_ml/Data/tfidf.pkl')


    def myfunc(self,q,key):
        cleanQuery=self.tfidf.transform([clean(q)])
        res=self.le.inverse_transform(self.logreg.predict(cleanQuery))
        proba=self.logreg.predict_proba(cleanQuery)[0].max()
        if proba<0.50:
            res[0]='undefined'

        if q in ['sopra','steria','sopra steria']:
            res[0]='about'

        uq.addQuery(q, res[0], proba, key,'logreg')
        return self.chatdata[self.chatdata['Intent'] == res[0]].iloc[0].answer




    def helpfunc(self):
        l=list(self.le.classes_)
        l.remove('same')
        l.remove('greeting')
        l.remove('undefined')
        s="You can ask me about- "+", ".join([ele.replace('_'," ").title() for ele in l])
        return s



        # if res[0]!='yes' or res[0]!='no':
        #     self.prevIntent=res[0]
        #     return self.chatdata[self.chatdata['Intent']==res[0]].answer
        # elif res[0]=='yes':
        #     return self.chatdata[self.chatdata['Intent'] == self.prevIntent].link
        # elif res[0]=='no':
        #     return "You can ask me something else"






lr=Lregression()
