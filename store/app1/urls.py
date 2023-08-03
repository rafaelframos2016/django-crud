from django.urls import path
from .views import index,criar

urlpatterns = [
    path('',index,  name='index'),
    path('criar/',criar,  name='criar'),
]