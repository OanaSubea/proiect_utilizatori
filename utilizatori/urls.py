from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = 'utilizatori'

urlpatterns = [
    url(r'^utilizatori/(?P<utilizatoriyid>\d+)/$', views.list, name='lista_utilizatori'),
    re_path('^$', views.list, name='lista_utilizatori'),
    ]