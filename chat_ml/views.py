from string import ascii_uppercase

from django.shortcuts import render,HttpResponse,render_to_response
from .Model.deeplearn import *
from .Model.regression import *
from random import choice




# Create your views here.



def home(request):
    if 'key' not in request.session:
        request.session['key'] = ''.join(choice(ascii_uppercase) for i in range(10))
    if request.is_ajax():
        q=request.POST['query']
        ans=lr.myfunc(q,request.session['key'])
        return HttpResponse(ans)

    return render(request,'chat_ml/chatengine.html',{'name':'manobhav'})


def tensorflow(request):
    if request.is_ajax():
        q=request.POST['query']
        ans=tensor.getResult(q)
        return HttpResponse(ans)

    return render(request,'chat_ml/chatengine.html',{'name':'manobhav'})