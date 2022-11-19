from pemira_ff.models import Token
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os
import json

class Command(BaseCommand):
    help = 'Load tokens'

    def handle(self, *args, **kwargs):
        current_dir = os.path.dirname(__file__)

        with open(current_dir + "/../../files/token.json") as file:
            data = json.load(file)
            for i in data:
                try:
                    Token.objects.get(tokenField=i['tokenField'])
                    self.stdout.write(f"{i['npm']} already exists")
                except:
                    try:
                        userObj = User.objects.create(username=i['tokenField'], password=f"PW{i['tokenField'][0:2]}{i['name'][0:2]}{i['npm'][0:2]}")
                    except:
                        pass
                        
                    tokenObj = Token.objects.create(user=userObj, tokenField=i['tokenField'], npm=i['npm'], name=i['name'], used=False)
                    self.stdout.write(f"create {i['npm']}: {i['tokenField']}")
