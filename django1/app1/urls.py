from django.urls import path
from app1.views import home,api1
urlpatterns=[
    path("",home),
    path("api1",api1),
]