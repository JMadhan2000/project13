from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('respose/',response,name='response'),
]