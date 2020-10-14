from django.core.management.base import BaseCommand, CommandError
import requests
from datetime import datetime
startTime = datetime.now()

class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(1000):
            requests.get('http://localhost:7777/web/')
        print(datetime.now() - startTime)