from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Token, Candidate, CType
import datetime

# Create your views here.
def home(req):
    context = {
        "today": datetime.date.today().strftime("%d %B %Y")
    }
    return render(req, "home.html", context)

def login_user(req):
    if req.method == "POST":
        token = req.POST.get("token")
        try:
            tokenObj = Token.objects.get(tokenField=token)
        except:
            return HttpResponseBadRequest()

        login(req, tokenObj.user)

        response = {
            "nama": tokenObj.user.username
        }

        return JsonResponse(response)

    return HttpResponseBadRequest()

@login_required(login_url = "/")
@csrf_exempt
def logout_user(req):
    logout(req)
    return HttpResponse()

# @login_required(login_url = "/")
def profil_anggota_bpm(req):
    calon_bpm = Candidate.objects.filter(cType=CType.BPM)
    context = {
        "calon": calon_bpm
    }
    return render(req, "profil-anggota-bpm.html", context)

# @login_required(login_url = "/")
def profil_anggota_bem(req):
    calon_bem = Candidate.objects.filter(cType=CType.BEM)
    context = {
        "calon": calon_bem
    }
    return render(req, "profil-anggota-bem.html", context)

# @login_required(login_url = "/")
def vote_anggota_bpm(req):
    calon_bpm = Candidate.objects.filter(cType=CType.BPM)
    context = {
        "calon": calon_bpm
    }
    return render(req, "vote-anggota-bpm.html", context)

# @login_required(login_url = "/")
def vote_anggota_bem(req):
    calon_bem = Candidate.objects.filter(cType=CType.BEM)
    context = {
        "calon": calon_bem
    }
    return render(req, "vote-anggota-bem.html", context)