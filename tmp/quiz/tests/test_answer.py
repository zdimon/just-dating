# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
class QuizTestAnswerCase(TestCase):
    #def setUp(self):
    #    Page.objects.create(title="test", content="bla bla", alias="index")
    #    #Animal.objects.create(name="cat", sound="meow")

    def test_create_room(self):
        print 'creating room test'
        self.assertEqual(1,1)