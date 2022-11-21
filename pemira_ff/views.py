from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .models import Token, Candidate, CType, VoteResult, Panitia
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
            if tokenObj.used:
                raise Exception()
        except:
            return HttpResponseBadRequest()

        login(req, tokenObj.user)

        response = {
            "nama": tokenObj.name
        }

        return JsonResponse(response)

    return HttpResponseBadRequest()

@login_required(login_url = "/")
@csrf_exempt
def logout_user(req):
    tokenObj = Token.objects.get(user=req.user)

    logout(req)

    tokenObj.used = True
    tokenObj.save()

    return HttpResponse()

@login_required(login_url = "/")
def profil_anggota_bpm(req):
    calon_bpm = Candidate.objects.filter(cType=CType.BPM)
    context = {
        "calon": calon_bpm
    }
    return render(req, "profil-anggota-bpm.html", context)

@login_required(login_url = "/")
def profil_ketua_bem(req):
    calon_bem = Candidate.objects.filter(cType=CType.BEM)
    context = {
        "calon": calon_bem
    }
    return render(req, "profil-anggota-bem.html", context)

@login_required(login_url = "/")
def vote_anggota_bpm(req):
    calon_bpm = Candidate.objects.filter(cType=CType.BPM)
    context = {
        "calon": calon_bpm
    }
    return render(req, "vote-anggota-bpm.html", context)

@login_required(login_url = "/")
def vote_ketua_bem(req):
    calon_bem = Candidate.objects.filter(cType=CType.BEM)
    context = {
        "calon": calon_bem
    }
    return render(req, "vote-anggota-bem.html", context)

@login_required(login_url = "/")
@csrf_exempt
def vote_anggota_bpm_post(req):
    if req.method == "POST":
        idBpm = int(req.POST.get("idBpm"))

        if idBpm == 0:
            voteObj, created = VoteResult.objects.get_or_create(candidate__isnull=True, cType=CType.BPM)
        else:
            voteObj, created = VoteResult.objects.get_or_create(candidate=Candidate.objects.get(cNo=idBpm, cType=CType.BPM), cType=CType.BPM)

        voteObj.count = voteObj.count + 1
        voteObj.save()

        return HttpResponse()

    return HttpResponseBadRequest()

@login_required(login_url = "/")
@csrf_exempt
def vote_ketua_bem_post(req):
    if req.method == "POST":
        idBem = int(req.POST.get("idBem"))

        if idBem == 0:
            voteObj, created = VoteResult.objects.get_or_create(candidate__isnull=True, cType=CType.BEM)
        else:
            voteObj, created = VoteResult.objects.get_or_create(candidate=Candidate.objects.get(cNo=idBem, cType=CType.BEM), cType=CType.BEM)

        voteObj.count = voteObj.count + 1
        voteObj.save()

        return HttpResponse()

    return HttpResponseBadRequest()

def done(req):
    return render(req, "done.html")

def hasil(req):
    return render(req, "dashboard-panitia.html")

@login_required(login_url = "/panitia")
def hasil_anggota_bpm(req):
    return render(req, "hasil-bpm.html")

@login_required(login_url = "/panitia")
def hasil_anggota_bpm_get(req):
    votes = VoteResult.objects.filter(cType=CType.BPM)

    vote_cnt = {}
    for vote in votes:
        if not vote.candidate:
            vote_cnt["Kosong"] = vote.count
        else:
            vote_cnt[vote.candidate.name] = vote.count

    return JsonResponse(vote_cnt)

@login_required(login_url = "/panitia")
def hasil_ketua_bem(req):
    return render(req, "hasil-bem.html")

@login_required(login_url = "/panitia")
def hasil_ketua_bem_get(req):
    votes = VoteResult.objects.filter(cType=CType.BEM)

    vote_cnt = {}
    for vote in votes:
        if not vote.candidate:
            vote_cnt["Kosong"] = vote.count
        else:
            vote_cnt[vote.candidate.name] = vote.count

    return JsonResponse(vote_cnt)

def panitia(req):
    if req.user.is_authenticated and isinstance(req.user, Panitia):
        return HttpResponseRedirect("/token")

    logout(req)

    return render(req, "panitia.html")

def panitia_login(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        try:
            panitiaObj = Panitia.objects.get(username=username, password=password)
        except:
            return HttpResponseBadRequest()

        login(req, panitiaObj)

        return HttpResponse()

    return HttpResponseBadRequest()

@login_required(login_url = "/panitia")
def panitia_dashboard(req):
    return render(req, "token.html")

def all_token(req):
    tokens = Token.objects.all()

    tokenList = []
    for token in tokens:
        tokenList.append({
            "id": token.pk,
            "token": token.tokenField,
            "npm": token.npm,
            "name": token.name,
            "used": token.used
        })

    res = {"tokenList": tokenList}

    return JsonResponse(res)

@login_required(login_url = "/panitia")
@csrf_exempt
def toggle_token(req):
    if req.method == "POST":
        try:
            token = req.POST.get("token")
            tokenObj = Token.objects.get(tokenField=token)
        except:
            return HttpResponseBadRequest()

        tokenObj.used = not tokenObj.used
        tokenObj.save()

        return HttpResponse()

    return HttpResponseBadRequest()