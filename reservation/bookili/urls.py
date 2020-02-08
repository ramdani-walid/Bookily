from django.urls import path
from . import views
app_name ='bookili'
urlpatterns = [
    path('',views.Accueil,name='accueil'),
    path('inscription/',views.inscription,name='inscription'),
    path('InscriptionClient/',views.InscriptionClient,name='InscriptionClient'),
    path('connexion/',views.connexion,name='connexion'),
    path('ConnexionClient/',views.ConnexionClient,name='ConnexionClient'),
    path('deconnexion/',views.deconnexion,name='deconnexion'),
    path('features/',views.Accueil,name='features'),
    path('tarifs/',views.Accueil,name='tarifs'),
    path('inscription/structure/',views.CreateStructure,name='structure'),
    path('inscription/structure/service/',views.Service,name='service'),
    path('inscription/structure/service/staff/',views.CreateStaff,name='staff'),
    path('connexion/profile/DetailStructure/<int:id>',views.AfficherStructure,name ='AfficherStructure'),
    path('connexion/profile/DetailStaff/<int:id>',views.AfficherStaff,name ='AfficherStaff'),
    path('profile/',views.Profile,name='Profile'),
    path('proprietaire/',views.All,name='All'),
]
