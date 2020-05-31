from django.shortcuts import render
from bs4 import BeautifulSoup
from backend.settings import BASE_DIR
import os


def index_web(request):
    path = os.path.join(BASE_DIR, 'static','front_dist','web','index.html')
    with open(path,'r') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    out = []
    for js in soup.find_all('script'):
        script_item = []
        try:
            type = js['type']
            script_item.append(' type="%s"' % js['type'])
        except:
            pass

        try:
            type = js['defer']
            script_item.append(' defer ')
        except:
            pass

        try:
            type = js['nomodule']
            script_item.append(' nomodule ')
        except:
            pass

        script_item.append('src="%s"' % js['src'])
        out_html = '<script'+' '.join(script_item)+'></script>'
        print(script_item)
        out.append(out_html)
    print(out)

    return render(request, 'index_web.html',{'scripts': out})

def index_mobi(request):
    path = os.path.join(BASE_DIR, 'static','front_dist','mobi','index.html')
    with open(path,'r') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    out = []
    for js in soup.find_all('script'):
        script_item = []
        try:
            type = js['type']
            script_item.append(' type="%s"' % js['type'])
        except:
            pass

        try:
            type = js['defer']
            script_item.append(' defer ')
        except:
            pass

        try:
            type = js['nomodule']
            script_item.append(' nomodule ')
        except:
            pass

        script_item.append('src="%s"' % js['src'])
        out_html = '<script'+' '.join(script_item)+'></script>'
        print(script_item)
        out.append(out_html)
    print(out)

    return render(request, 'index_mobi.html',{'scripts': out})