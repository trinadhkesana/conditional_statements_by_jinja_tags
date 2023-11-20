from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'conditions.html',context=d)