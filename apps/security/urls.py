
from django.conf.urls import patterns, url
from .views import Login
 
urlpatterns = patterns('',
    url('login', Login.as_view(), name="login"),                
)