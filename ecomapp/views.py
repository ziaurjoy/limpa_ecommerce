from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request,'fontend/pages/home.html',context)