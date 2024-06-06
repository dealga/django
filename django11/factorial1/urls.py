from django.urls import path
from factorial1.views import home
urlpatterns = [path('', home),]