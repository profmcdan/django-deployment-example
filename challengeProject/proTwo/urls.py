from django.conf.urls import url
from proTwo import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^help/', views.help, name='help'),
    url(r'^users/', views.user, name='user'),
]
