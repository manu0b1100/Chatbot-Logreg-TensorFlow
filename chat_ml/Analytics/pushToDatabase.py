from chat_ml.models import *
import datetime
class UserQ:

    def addQuery(self,query,intent,prob,key):
        q=UserQuery(query=query,pclass=intent,prob=prob,date=datetime.datetime.now(),session=key)
        q.save()





uq=UserQ()



