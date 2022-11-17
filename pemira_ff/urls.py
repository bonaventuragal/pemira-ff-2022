from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout_user'),
    path('profil/anggota-bpm/', profil_anggota_bpm, name='profil_anggota_bpm'),
    path('profil/anggota-bem/', profil_anggota_bem, name='profil_anggota_bem'),
    path('vote/anggota-bpm/', vote_anggota_bpm, name='vote_anggota_bpm'),
    path('vote/anggota-bem/', vote_anggota_bem, name='vote_anggota_bem'),
]