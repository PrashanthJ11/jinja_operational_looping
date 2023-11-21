from django.shortcuts import render

# Create your views here.
def for_loop(request):
    d={'name':'Prashanth Rishi'}
    return render(request,'for_loop.html',d)
