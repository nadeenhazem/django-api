from django.urls import path
from .views import *
urlpatterns = [

    path('insert/', insert, name='insert'),
    path('list', List, name='alllist'),
    path('list/<id>', GETTRAINEE, name='listid'),
    path('update/', update),
    path('delete/<id>', delete),
]
