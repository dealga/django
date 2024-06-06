from django.urls import path
from oddeven.views import home
urlpatterns = [path('', home),]