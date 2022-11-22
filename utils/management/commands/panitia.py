from pemira_ff.models import Panitia
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create Panitia'

    def handle(self, *args, **kwargs):
        try:
            Panitia.objects.get_or_create(username="pemiraff22", password="pemiraff22")
        except:
            pass

        self.stdout.write("username: pemiraff22")
        self.stdout.write("password: pemiraff22")