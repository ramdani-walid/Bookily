from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Proprietaire, Structure as StructureModel
from .forms import Inscription, Structure,ServiceForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def Accueil(request):
    return render(request,'pages/accueil.html')

def Service(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit= False)
        instance.userpropr_id = request.user
        instance.save()
        return redirect('/')
    return render(request,'pages/service.html',{'form':form})

@login_required
def CreateStructure(request):
    form = Structure(request.POST or None)
    if form.is_valid():
        instance = form.save(commit= False)
        instance.userpropr = request.user
        instance.save()
        return redirect('service/',locals())
        form = Structure()
    return render (request,'pages/structure.html',{'form':form})

    # req = request.user
def AfficherStructure (request,id):
    structure = StructureModel.objects.get(userpropr_id=id)
    # for s in (StructureModel.objects.raw('SELECT * FROM STRUCTURE,auth_user WHERE userpropr_id = auth_user.id')):
    #     s.username = request.user
    #     req = s.username
    # print(s[0].adresse_struct)
    return render(request,'pages/afficherstructure.html',{'structure':structure})

def inscription(request):
    if request.method =="POST":
        form = Inscription(request.POST or None)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,"bienvenue:")
            login(request, user)
            # form = Inscripion()
            return redirect('structure/',locals())
    else :
        form = Inscription()
    return render(request,'pages/inscription.html',{'form':form})

def connexion(request):
    template ='profile/'
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username ,password = password)
            print(user)
            if user is not None:
                login(request,user)
                messages.success(request,'vous etes bien connecté !')
                # return redirect('/bookili',locals())
                return redirect(template,locals())

            else :
                messages.error(request,'compte invalid !')
        else :
            messages.error(request,'compte invalid !')
    else :
        form = AuthenticationForm()
    return render(request,'pages/connexion.html',{'form':form})


def deconnexion(request):
      logout(request)
      return redirect('/bookili')


def Profile (request):
    profil = User.objects.get(username=request.user)
    return render(request,'pages/profile.html',{'profil':profil})
