from django.shortcuts import render

# Create your views here.
  
def forloop(request):
    d={'a':[10,20],'name':'mine'}
    return render(request,'just.html',d)