from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Panitia(User):
    class Meta:
        proxy: True

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tokenField = models.CharField(max_length=5, unique=True)
    npm = models.CharField(max_length=10, null=True, unique=True)
    used = models.BooleanField()
    name = models.CharField(max_length=100, null=True)

class CType(models.IntegerChoices):
    BPM = 1
    BEM = 2

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    photoPath = models.CharField(max_length=100)
    visi = models.TextField()
    misi = models.TextField()
    cType = models.IntegerField(choices=CType.choices)
    cNo = models.IntegerField(default=0)

class VoteResult(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, blank=True)
    count = models.IntegerField(default=0)
    cType = models.IntegerField(choices=CType.choices, default=1)