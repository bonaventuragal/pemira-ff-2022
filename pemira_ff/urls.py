from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/npm/', login_npm, name='login_npm'),
    path('login/<str:npm>/', login_token, name='login_token'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout_user'),
    path('profil/anggota-bpm/', profil_anggota_bpm, name='profil_anggota_bpm'),
    path('profil/ketua-bem/', profil_ketua_bem, name='profil_ketua_bem'),
    path('vote/anggota-bpm/', vote_anggota_bpm, name='vote_anggota_bpm'),
    path('vote/ketua-bem/', vote_ketua_bem, name='vote_ketua_bem'),
    path('vote/anggota-bpm/post/', vote_anggota_bpm_post, name='vote_anggota_bpm_post'),
    path('vote/ketua-bem/post/', vote_ketua_bem_post, name='vote_ketua_bem_post'),
    path('done/', done, name='done'),
    path('panitia/dashboard/', panitia_dashboard, name='panitia_dashboard'),
    path('hasil/anggota-bpm/', hasil_anggota_bpm, name='hasil_anggota_bpm'),
    path('hasil/anggota-bpm/get/', hasil_anggota_bpm_get, name='hasil_anggota_bpm_get'),
    path('hasil/ketua-bem/', hasil_ketua_bem, name='hasil_ketua_bem'),
    path('hasil/ketua-bem/get/', hasil_ketua_bem_get, name='hasil_ketua_bem_get'),
    path('panitia/', panitia, name='panitia'),
    path('panitia/login/', panitia_login, name='panitia_login'),
    path('panitia/logout/', panitia_logout, name='panitia_logout'),
    path('token/', token, name='token'),
    path('token/all/', all_token, name='all_token'),
    path('token/toggle/', toggle_token, name='toggle_token'),
]