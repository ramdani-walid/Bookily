from django import forms
from django.contrib.auth.models import User
from .models import Proprietaire, Structure as StructureModel, Service, Staff, Servir, Client as ClientModel, CatergorieStructure
from django.contrib.auth.forms import UserCreationForm

#Inscripion compte user (Propriétaire)
class Inscription(UserCreationForm):
    # mot_de_passe = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(label='Utilisateur')
    password1 = forms.CharField(help_text=False,label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(help_text=False,label='confirmation password',widget=forms.PasswordInput)

    class Meta:
        model = User
        # fields = '__all__'
        fields =('username','email','password1','password2',)


class Structure(forms.ModelForm):
    catergorie_structure_idcatergorie_structure = forms.ModelChoiceField(queryset=CatergorieStructure.objects.all(),label='catégorie')
    class Meta:
        model = StructureModel
        # fields = '__all__'
        fields = ('nom_struct','adresse_struct','catergorie_structure_idcatergorie_structure','code_postal',)

class ServiceForm(forms.ModelForm):
    # structure_idstructure = forms.CharField(label='structure')
    debut_service = forms.TimeField(help_text='09:00')
    fin_service = forms.TimeField(help_text='11:00')
    structure_idstructure =forms.ModelChoiceField(queryset=StructureModel.objects.all(),label='type structure')

    class Meta:
        model = Service
        fields = ('nom_service','debut_service','fin_service','structure_idstructure',)
        # exclude =('structure_idstruc
class StaffForm(forms.ModelForm):
    structure_idstructure =forms.ModelChoiceField(queryset=StructureModel.objects.all(),label='type structure')
    
    class Meta:
        model = Staff
        # fields ='__all__'
        fields = ('nom_staff','prenom_staff','structure_idstructure',)

#
# class ServirForm(forms.ModelForm):
#     class Meta:
#         model = Servir
#         fields = '__all__'


#Inscripion compte Client :
class InscriptionClientForm(forms.ModelForm):
    mot_de_passe_client = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ClientModel
        fields =('nom_client','email','mot_de_passe_client',)


class ConnexionClientForm(forms.ModelForm):
    mot_de_passe_client = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ClientModel
        fields =('email','mot_de_passe_client',)
