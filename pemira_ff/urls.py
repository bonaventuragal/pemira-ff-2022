from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout_user'),
    path('profil/anggota-bpm/', profil_anggota_bpm, name='profil_anggota_bpm'),
    path('profil/ketua-bem/', profil_ketua_bem, name='profil_ketua_bem'),
    path('vote/anggota-bpm/', vote_anggota_bpm, name='vote_anggota_bpm'),
    path('vote/ketua-bem/', vote_ketua_bem, name='vote_ketua_bem'),
    path('vote/anggota-bpm/post/', vote_anggota_bpm_post, name='vote_anggota_bpm_post'),
    path('vote/ketua-bem/post/', vote_ketua_bem_post, name='vote_ketua_bem_post'),
    path('done/', done, name='done'),
]