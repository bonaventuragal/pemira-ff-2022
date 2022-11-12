from django.shortcuts import render
import datetime

# Create your views here.
def home(req):
    context = {
        "today": datetime.date.today().strftime("%d %B %Y")
    }
    return render(req, 'home.html', context)