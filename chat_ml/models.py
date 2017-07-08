from django.db import models
# Create your models here.
class UserQuery(models.Model):
    query=models.CharField(max_length=1000)
    date=models.DateTimeField()
    pclass=models.CharField(max_length=20,default='about')
    session=models.CharField(max_length=10,default='0000')
    prob=models.FloatField(default=0.0)
    backend=models.CharField(max_length=10,default='logreg')


    def __str__(self):
        return self.query






