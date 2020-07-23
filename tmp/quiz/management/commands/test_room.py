# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from quiz.models.models import *
from dj.settings import BASE_DIR
import os
import json
from quiz.utils import define_winner

class Command(BaseCommand):
    def handle(self, *args, **options):
       room = Room.objects.get(pk=21)
       define_winner(room)
