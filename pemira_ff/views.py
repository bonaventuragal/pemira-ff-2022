from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Token
import datetime

# Create your views here.
def home(req):
    context = {
        "today": datetime.date.today().strftime("%d %B %Y")
    }
    return render(req, 'home.html', context)

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

@login_required(login_url="/home")
@csrf_exempt
def logout_user(req):
    logout(req)
    return HttpResponse()