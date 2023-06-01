from django.urls import path
from srh.views import *

app_name='srh'

urlpatterns=[
    path('warner/',warner,name='warner'),
]