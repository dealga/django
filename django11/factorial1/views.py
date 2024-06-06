#from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'factorial1/index.html',{'param1':"hello world"})




#from django.shortcuts import render
#def home(request):
#    result=1
#    n1=5
#    for i in range(1,n1+1,1):
#        result=result*i
#    return render(request,'factorial1/index.html',{'param1':result,'param2':n1})


from django.shortcuts import render
from factorial1.forms import inputform
def home(request):
    result=0
    n1=0
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            
            result=fact(n1)
            return render(request,"factorial1/index.html",{'param1':result, 'param2':n1, 'form':form1})
    else:
        form1=inputform()
    return render(request,"factorial1/index.html",{'param1':result, 'param2':n1, 'form':form1})

def fact(n1):  
    result=1
    for i in range(1,n1+1,1):
        result=result*i
    return result
