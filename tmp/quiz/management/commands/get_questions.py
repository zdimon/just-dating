# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError
import os
import io
import json
from dj.settings import BASE_DIR
import time


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--from',
            dest='from',
            help='Start from category index',
        )

        parser.add_argument(
            '--to',
            dest='to',
            help='End on category index',
        )

    def parse(self, _from, _to):
        cur_file = _from
        base_url = 'https://baza-otvetov.ru'
        r = requests.get(base_url + '/categories')
        bs = BeautifulSoup(r.text, "html.parser")
        content = bs.find("div", {"class": "content"})
        blocks = content.find_all("div", {"class": "block"})
        categories = []
        questions = []
        for block in blocks:
            categories.append(block.a['href'])

        if _to != 29:
            for i in range(1, 29 - _to):
                categories.pop(-1)
        if _from != 1:
            for i in range(1, _from):
                categories.pop(0)

        for category in categories:
            time.sleep(3)
            r = requests.get(base_url + category)
            bs = BeautifulSoup(r.text, "html.parser")
            q_list = bs.find("div", {"class": "q-list"})
            name = q_list.find("caption").h2.text.split("(")[0].strip()
            print("Current category: " + name)
            trs = q_list.find_all("tr", {"class": "tooltip"})
            _question = []
            for tr in trs:
                td = tr.find_all("td")
                _question.append({"question": td[1].text.strip(), "answer": td[2].text.strip()})
            try:
                pages = int(q_list.find("div", {"class": "q-list__nav"}).find_all("a")[-1]['href'].split("/")[-1])
            except IndexError:
                pages = 0
            page = 0
            while page != pages:
                print("Pages left: " + str((pages - page) / 10))
                time.sleep(1)
                _r = requests.get("%s%s/%s" % (base_url, category, page + 10))
                _bs = BeautifulSoup(_r.text, "html.parser")
                q_list = _bs.find("div", {"class": "q-list"})
                trs = q_list.find_all("tr", {"class": "tooltip"})
                for tr in trs:
                    td = tr.find_all("td")
                    _question.append({"question": td[1].text.strip(), "answer": td[2].text.strip()})
                page += 10
            # questions.append({"category": name, "questions": _question})
            with io.open(os.path.join(BASE_DIR, "quiz", "data", "questions", str(cur_file) + ".json"), "w",
                         encoding='utf8') as file:
                data = json.dumps({"category": name, "questions": _question}, ensure_ascii=False, encoding='utf8')
                file.write(unicode(data))
                cur_file += 1

    def handle(self, *args, **options):
        _from = 1
        _to = 29
        if options['from']:
            _from = int(options['from'])
        if options['to']:
            _to = int(options['to'])
        self.parse(_from, _to)
