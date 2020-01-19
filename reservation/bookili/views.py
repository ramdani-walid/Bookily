from django.shortcuts import render, redirect
from .models import Proprietaire, Structure
from .forms import Inscription, Structure
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def afficher(request):
    return render(request,'pages/accueil.html')


def inscription(request):
        form = Inscription(request.POST or None )
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            print(user)
            user.save()
            # form = Inscription()
            return redirect("structure/")
        return render(request,'pages/inscription.html',{'form':form})

def structure(request):
    form = Structure(request.POST or None)
    if form.is_valid():
        instance = form.save(commit= False)
        instance.userpropr = request.user
        instance.save()
        form = Structure()
    return render (request,'pages/structure.html',{'form':form})

def welcome (request):
    return render (request,'pages/welcome.html')
