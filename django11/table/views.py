from django.shortcuts import render
from django.http import HttpResponse
def toble(request):
    num=5
    table=""
    for i in range(1,21):
    
        for j in range(1,11):
            result=i*j
            table+=f"{i}*{j}={result}\n<br>"
        table+="<br>"
    return HttpResponse(table)









