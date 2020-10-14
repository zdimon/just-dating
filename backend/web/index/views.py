from django.shortcuts import render
import requests


def main_page(request):
    return render(requests, 'web/index.html')