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
    path('vote/anggota-bpm/post/', vote_anggota_bpm_post, name='vote_anggota_bpm_post'),
    path('vote/anggota-bem/post/', vote_anggota_bem_post, name='vote_anggota_bem_post'),
    path('done/', done, name='done'),
    path('hasil/', hasil, name='hasil'),
    path('hasil/anggota-bpm/', hasil_anggota_bpm, name='hasil_anggota_bpm'),
    path('hasil/anggota-bpm/get/', hasil_anggota_bpm_get, name='hasil_anggota_bpm_get'),
    path('hasil/ketua-bem/', hasil_ketua_bem, name='hasil_ketua_bem'),
    path('hasil/ketua-bem/get/', hasil_ketua_bem_get, name='hasil_ketua_bem_get'),
]