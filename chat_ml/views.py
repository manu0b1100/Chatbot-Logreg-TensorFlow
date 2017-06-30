from django.shortcuts import render
from django.shortcuts import render,HttpResponse,render_to_response
from django.shortcuts import render, redirect
from .Model.deeplearn import *
from .Model.regression import *
from .Model.wordpred import *
from .models import *
from sklearn.feature_extraction.text import CountVectorizer


# Create your views here.

def testfunc(request):


    return HttpResponse("Aur bhai")

def home(request):
    if request.is_ajax():
        q=request.POST['query']
        ans=lr.myfunc(q)
        return HttpResponse(ans)

    return render(request,'chat_ml/chatengine.html',{'name':'manobhav'})


def getnextword(request):
    if request.is_ajax():
        q=request.POST['query']
        ans=getResultList(q)
        return HttpResponse(ans)


def getPred(request):
    '''if request.is_ajax():
        q=request.POST['query']
        q=q.split()
        p=""
        if len(q)>0:
            q=q[-1]
            create_n_insert()
            p=getTrieResults(q)
        return HttpResponse(p)'''
    pass

def tensorflow(request):
    if request.is_ajax():
        q=request.POST['query']
        ans=tensor.getResult(q)
        return HttpResponse(ans)

    return render(request,'chat_ml/chatengine.html',{'name':'manobhav'})