from chat_ml.models import *
import datetime
class UserQ:

    def addQuery(self,query,intent,prob,key,backend):
        q=UserQuery(query=query,pclass=intent,prob=prob,date=datetime.datetime.now(),session=key,backend=backend)
        q.save()





uq=UserQ()



