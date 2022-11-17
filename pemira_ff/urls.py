from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout_user'),
    path('profil/anggota-bpm/', profil_anggota_bpm, name='profil_anggota_bpm'),
    path('profil/anggota-bem/', profil_anggota_bem, name='profil_anggota_bem'),
]