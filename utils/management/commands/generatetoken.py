from pemira_ff.models import Token
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import random
import string
import os

def tokengen():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

class Command(BaseCommand):
    help = 'Create tokens'

    def handle(self, *args, **kwargs):
        current_dir = os.path.dirname(__file__)
        
        with open(current_dir + "/../../files/mhs.csv") as file:
            for line in file:
                line = line.rstrip()
                npm, nama = line.split(',')

                # skip existing user
                try:
                    tokenObj = Token.objects.get(npm=npm)
                    self.stdout.write(f"{npm} already exists")
                    continue
                except:
                    pass

                # create new token
                token = None
                while token is None:
                    try:
                        token = tokengen()
                        tokenObj = Token.objects.get(tokenField=token)
                        token = None
                    except:
                        pass

                # create token and user
                try:
                    userObj = User.objects.create(username=token, password=f"PW{token[0:2]}{nama[0:2]}{npm[0:2]}")
                except:
                    pass
                    
                tokenObj = Token.objects.create(user=userObj, tokenField=token, npm=npm, name=nama, used=False)
                self.stdout.write(f"create {npm}: {token}")