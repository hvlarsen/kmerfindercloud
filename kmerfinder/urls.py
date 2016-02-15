from django.conf.urls import url

from . import views

app_name = 'kmerfinder'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^kmerfinder/$', views.DetailView, name='detail'),
]