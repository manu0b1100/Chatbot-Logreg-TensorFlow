from django.shortcuts import render,HttpResponse,render_to_response
from .Model.deeplearn import *
from .Model.regression import *



# Create your views here.



def home(request):
    if request.is_ajax():
        q=request.POST['query']
        ans=lr.myfunc(q)
        return HttpResponse(ans)

    return render(request,'chat_ml/chatengine.html',{'name':'manobhav'})


def tensorflow(request):
    if request.is_ajax():
        q=request.POST['query']
        ans=tensor.getResult(q)
        return HttpResponse(ans)

    return render(request,'chat_ml/chatengine.html',{'name':'manobhav'})