import pandas as pd
from chat_ml.Model.tokenize_stem import cleanAndMerge
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import linear_model
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
import tflearn
import tensorflow as tf


def processdata(chatdata):
    newchatdata=pd.DataFrame(columns=['Intent','question','answer'])
    for i in range(0,chatdata['question'].size):
        for sent in chatdata['question'][i].split(','):
            newchatdata=newchatdata.append({'Intent':chatdata['Intent'][i].lower(),'question':sent,'answer':chatdata['answer'][i]},ignore_index=True)
    return newchatdata


def preprocessDataMaster():
    chatdata = pd.read_excel("chat_ml/Data/chatbotdata.xlsx", columns=['intent', 'question', 'answer'])
    chatdata = processdata(chatdata)
    chatdata['corpus'] = cleanAndMerge(chatdata['question'])
    # for i in range(0,3):
    #     chatdata['corpus'][i]=chatdata['question'][i]
    chatdata.to_csv('chat_ml/Data/processedchatdata.csv', index=False)

def LogRegTraining():
    chatdata = pd.read_csv("chat_ml/Data/processedchatdata.csv", converters={'corpus': str})
    tfidf = TfidfVectorizer(ngram_range=(1, 3))
    tfidf.fit(chatdata['corpus'])
    train_corpus_tfidf = tfidf.transform(chatdata['corpus'])
    le = preprocessing.LabelEncoder()
    Numeric_Intents = le.fit_transform(chatdata['Intent'])
    logreg = linear_model.LogisticRegression(C=1e5)
    logreg.fit(train_corpus_tfidf.toarray(), Numeric_Intents)
    joblib.dump(logreg, 'chat_ml/Data/logistic.pkl')
    joblib.dump(tfidf, 'chat_ml/Data/tfidf.pkl')
    joblib.dump(le, 'chat_ml/Data/lencoder.pkl')

def TensorTraining():
    tf.reset_default_graph()
    chatdata = pd.read_csv("chat_ml/Data/processedchatdata.csv", converters={'corpus': str})
    cv = CountVectorizer(ngram_range=(1, 3))
    cv.fit(chatdata['corpus'])
    train_corpus_cv = cv.transform(chatdata['corpus'])
    cv1 = CountVectorizer()
    cv1.fit(chatdata['Intent'])
    class_corpus_cv = cv1.transform(chatdata['Intent'])
    net = tflearn.input_data(shape=[None, len(train_corpus_cv.toarray()[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(class_corpus_cv.toarray()[0]), activation='softmax')
    net = tflearn.regression(net)
    model = tflearn.DNN(net, tensorboard_dir='chat_ml/Data/tflearn_logs')
    model.fit(train_corpus_cv.toarray(), class_corpus_cv.toarray(), n_epoch=500, batch_size=8, show_metric=True)
    model.save('chat_ml/Data/model.tflearn')
    joblib.dump(cv, 'chat_ml/Data/count_vector.pkl')
    joblib.dump(cv1, 'chat_ml/Data/class_count_vector.pkl')

