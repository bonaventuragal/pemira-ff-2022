from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Panitia(User):
    class Meta:
        proxy: True

class Token(User):
    tokenField = models.CharField(max_length=5)
    npm = models.CharField(max_length=10, null=True)
    used = models.BooleanField()
    name = models.CharField(max_length=100, null=True)

    class Meta:
        proxy: True

class CType(models.IntegerChoices):
    BPM = 1
    BEM = 2

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    photoPath = models.CharField(max_length=100)
    visi = models.TextField()
    misi = models.TextField()
    cType = models.IntegerField(choices=CType.choices)

class VoteResult(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    count = models.IntegerField()

    @property
    def cType(self):
        return self.candidate.cType