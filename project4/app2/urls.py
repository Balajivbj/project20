from django.urls import path
from app2.views import *
app_name='something'
urlpatterns=[
    path('app2/',app2,name='app2'),
]