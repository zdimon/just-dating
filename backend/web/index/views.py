from django.shortcuts import render
import requests
import json


def main_page(request):
    #res = requests.get('/v1/account/user_list')
    #data = json.loads(res.text)
    return render(request, 'web/index.html')



def homepage(request):
    #res = requests.get('http://localhost:8000/v1/account/user_list')
    #data = json.loads(res.text)
    return render(request, 'main/index.html',{})
