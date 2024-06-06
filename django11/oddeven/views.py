from django.shortcuts import render
from factorial1.forms import inputform
def home(request):
    n1=0
    result=""
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            result=oddoreven(n1)
            return render(request,"oddeven/index.html",{'param1':n1, 'param2':result, 'form':form1})
    else:
        form1=inputform()
    return render(request,"oddeven/index.html",{'param1':n1, 'param2':result, 'form':form1})

def oddoreven(n1):
    num=""
    if n1%2==0:
        num='even'
    else:
        num='odd'
    return num