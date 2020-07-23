# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from quiz.utils import create_test_quize

# Create your tests here.
class QuizTestRoomCase(TestCase):
    #def setUp(self):
    #    Page.objects.create(title="test", content="bla bla", alias="index")
    #    #Animal.objects.create(name="cat", sound="meow")

    def test_answer(self):
        create_test_quize()
        self.assertEqual(1,1)