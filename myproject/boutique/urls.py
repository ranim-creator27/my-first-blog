from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('nos-robes/', views.nos_robes, name='nos_robes'),
    path('ajouter-robe/', views.ajouter_robe, name='ajouter_robe'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('reserver_robe/', views.reserver_robe,name= 'reserver_robe'),
    path('reservation/success/', views.reservation_success, name='reservation_success'),
]