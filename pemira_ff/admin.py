from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Token)
admin.site.register(Panitia)
admin.site.register(Candidate)
admin.site.register(VoteResult)