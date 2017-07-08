
import tflearn
import tensorflow as tf
from sklearn.externals import joblib
import pandas as pd
from .tokenize_stem import clean
from chat_ml.Analytics.pushToDatabase import *

tf.reset_default_graph()


class tf:
    def __init__(self):
        self.cv = joblib.load('./chat_ml/Data/count_vector.pkl')
        self.cv1 = joblib.load('./chat_ml/Data/class_count_vector.pkl')
        self.chatdata = pd.read_csv("./chat_ml/Data/processedchatdata.csv",converters={'corpus':str})
        net = tflearn.input_data(shape=[None, len(self.cv.get_feature_names())])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(self.cv1.get_feature_names()), activation='softmax')
        net = tflearn.regression(net)
        self.model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
        self.model.load('./chat_ml/Data/model.tflearn')

    def getResult(self,q,key):
        query = q
        prediction = self.model.predict(self.cv.transform([clean(query)]).toarray())
        pclass = self.cv1.get_feature_names()[prediction.argmax()]

        if prediction.max()<0.50:
            pclass='undefined'

        if q in ['sopra','steria','sopra steria']:
            pclass='about'

        uq.addQuery(q, pclass, prediction.max(), key,'tensor')

        return self.chatdata[self.chatdata['Intent']==pclass].iloc[0].answer



tensor=tf()

