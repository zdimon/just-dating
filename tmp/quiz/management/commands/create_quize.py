# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
import os
import json
from quiz.utils import create_test_quize

class Command(BaseCommand):
    def handle(self, *args, **options):
        create_test_quize()