from django.conf.urls import url
from . import views

app_name = 'chatapp'

urlpatterns = [
url(r'^$', views.home, name='home'),
url(r'tensorflow', views.tensorflow, name='tensorflow')
        ]