from django.shortcuts import render

# Create your views here.
def afficher(request):
    return render(request,'pages/base.html')
