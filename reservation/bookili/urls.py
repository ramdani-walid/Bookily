from django.urls import path
from . import views
app_name ='bookili'
urlpatterns = [
    path('',views.Accueil,name='accueil'),
    path('inscription/',views.inscription,name='inscription'),
    path('connexion/',views.connexion,name='connexion'),
    path('deconnexion/',views.deconnexion,name='deconnexion'),
    path('features/',views.Accueil,name='features'),
    path('tarifs/',views.Accueil,name='tarifs'),
    path('inscription/structure/',views.CreateStructure,name='structure'),
    # path('connexion/DetailStructure/',views.AfficherStructure,name='AfficherStructure'),
    # path('connexion/structure/service/',views.Service,name='service'),
    path('inscription/structure/service/',views.Service,name='service'),
    path('connexion/profile/DetailStructure/<int:id>',views.AfficherStructure,name ='AfficherStructure'),
    path('connexion/profile/',views.Profile,name='Profile'),
]
