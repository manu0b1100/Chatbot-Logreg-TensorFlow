from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'chatapp'

urlpatterns = [
url(r'^$', views.home, name='home'),
url(r'tensorflow', views.tensorflow, name='tensorflow')
        ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)