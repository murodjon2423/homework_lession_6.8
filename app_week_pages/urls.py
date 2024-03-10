from django.urls import path

from .views import indexuz
from .views import indexen
from .views import indexru
from .views import index

urlpatterns=[
    path('weekday/en/', indexen,name='indexen_url'),
    path('weekday/ru/', indexru,name='indexru_url'),
    path('weekday/uz/', indexuz,name='indexuz_url'),
    path('weekday/', index,name='index_url')
]