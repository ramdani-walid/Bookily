from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Proprietaire, Structure as StructureModel, Service as ServiceModel, Staff as StaffModel, Servir, Client as ClientModel
from .forms import Inscription, Structure,ServiceForm, StaffForm, InscriptionClientForm, ConnexionClientForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist # pour gérer les exceptions

# Create your views here.
def Accueil(request):
    return render(request,'pages/accueil.html')

@login_required
def Service(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit= False)
        instance.userpropr_id = request.user
        instance.save()
        # return redirect('/bookili/connexion/profile')
        return redirect('staff/')
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

# @login_required
def CreateStaff(request):
    form = StaffForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit= False)
        instance.userpropr_id = request.user
        instance.save()
        return redirect('/bookili/profile/',locals())
        form = StaffForm()
    return render (request,'pages/staff.html',{'form':form})

# @login_required
# def AfficherService (request,id):
#     structure = StructureModel.objects.get(userpropr_id=id)
#     # for s in (StructureModel.objects.raw('SELECT * FROM STRUCTURE,auth_user WHERE userpropr_id = auth_user.id')):
#     #     s.username = request.user
#     #     req = s.username
#     # print(s[0].adresse_struct)
#     return render(request,'pages/afficherstructure.html',{'structure':structure})

@login_required
def AfficherStructure (request,id):
    try:
         structure = StructureModel.objects.filter(userpropr_id=id).all()
         service = ServiceModel.objects.filter(userpropr_id=id ).all()
    except ObjectDoesNotExist:
        return redirect ('/bookili/inscription/structure/service/')
        messages.error(request,'crée votre service')

    # for s in (StructureModel.objects.raw('SELECT * FROM STRUCTURE,auth_user WHERE userpropr_id = auth_user.id')):
    #     s.username = request.user
    #     req = s.username
    # print(s[0].adresse_struct)
    return render(request,'pages/afficherstructure.html',{'structure':structure,'service':service})


def AfficherStaff(request,id):
    try:
        staff = StaffModel.objects.filter(userpropr_id=id).all()
        print(staff)
    except ObjectDoesNotExist:
        messages.error(request,'ajout des staff')
        return redirect ('/bookili/inscription/structure/service/staff/')

    # for s in (StructureModel.objects.raw('SELECT * FROM STRUCTURE,auth_user WHERE userpropr_id = auth_user.id')):
    #     s.username = request.user
    #     req = s.username
    # print(s[0].adresse_struct)
    return render(request,'pages/afficherstaff.html',{'staff':staff})

#inscription compte Proprietaire de structure
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
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username ,password = password)
            if user is not None:
                login(request,user)
                messages.success(request,'vous etes bien connecté !')
                # return redirect('/bookili',locals())
                return redirect('/bookili/profile/',locals())

            else :
                messages.error(request,'compte invalid !')
        else :
            messages.error(request,'compte invalid !')
    else :
        form = AuthenticationForm()
    return render(request,'pages/connexion.html',{'form':form})


def deconnexion(request):
      logout(request)
      del request.session
      return redirect('/bookili')


def Profile(request):
    profil = User.objects.get(username=request.user)
    return render(request,'pages/profile.html',{'profil':profil})


#inscription compte Client de structure
def InscriptionClient(request):
        form = InscriptionClientForm(data=request.POST or None)
        if form.is_valid():
            instance = ClientModel()
            instance.nom_client = form.cleaned_data['nom_client']
            instance.email = form.cleaned_data['email']
            instance.mot_de_passe_client = form.cleaned_data['mot_de_passe_client']
            instance.save()
            return redirect('/bookili/proprietaire/',locals())
        else :
            form = InscriptionClientForm()
        return render(request,'pages/InscriptionClient.html',{'form':form})

def ConnexionClient(request):
        form = ConnexionClientForm(request.POST or None)
        if form.is_valid():
            email1 = form.cleaned_data.get('email')
            mot_de_passe_client = form.cleaned_data.get('mot_de_passe_client')
            if (ClientModel.objects.filter(email=email1).exists()):
                if (ClientModel.objects.filter(mot_de_passe_client=mot_de_passe_client).exists()):
                    print('succes connexion')
                    return redirect('/bookili/proprietaire',locals())
                else:
                    print('error mot de passe !')
            else:
                print('echec connexion')
        return render(request,'pages/ConnexionClient.html',{'form':form})


def DeconnexionClient(request):
      logout(request)
      return redirect('/bookili')


def All(request):
    all = StaffModel.objects.all()
    # structure = StructureModel.objects.all()
    return render (request,'pages/recherchestaff.html',{'all':all})
