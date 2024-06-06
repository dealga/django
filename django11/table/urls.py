from django.urls import path
from table.views import toble
urlpatterns = [path('', toble),]