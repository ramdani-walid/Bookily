from django import forms
from django.contrib.auth.models import User
from .models import Proprietaire, Structure, Service
from django.contrib.auth.forms import UserCreationForm


class Inscription(UserCreationForm):
    # mot_de_passe = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(label='Utilisateur')
    password1 = forms.CharField(help_text=False,label='password')
    password2 = forms.CharField(help_text=False,label='confirmation password')

    class Meta:
        model = User
        # fields = '__all__'
        fields =('username','email','password1','password2',)

class Structure(forms.ModelForm):
    # catergorie_structure_idcatergorie_structure = forms.CharField(label='categorie')

    class Meta:
        model = Structure
        # fields = '__all__'
        fields = ('nom_struct','adresse_struct','catergorie_structure_idcatergorie_structure','code_postal',)

class ServiceForm(forms.ModelForm):
    # structure_idstructure = forms.CharField(label='structure')
    duree_service = forms.TimeField(help_text='09:00')
    class Meta:
        model = Service
        fields = ('nom_service','duree_service','structure_idstructure',)
        # exclude =('structure_idstructure',)