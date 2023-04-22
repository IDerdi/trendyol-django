from django.urls import path
from .views import *

urlpatterns=[
    path('',index, name='index'),
    path('urun/<int:urunId>',urunDetay, name='detay')
]