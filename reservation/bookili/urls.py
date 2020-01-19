from django.urls import path
from . import views
app_name ='bookili'
urlpatterns = [
    path('',views.afficher,name='accueil'),
    path('inscription/',views.inscription,name='inscription'),
    path('login/',views.afficher,name='login'),
    path('features/',views.afficher,name='features'),
    path('tarifs/',views.afficher,name='tarifs'),
    path('inscription/structure/',views.structure,name='structure'),
    path('inscription/welcome/',views.welcome,name='welcome'),
]
