from django.shortcuts import render

def model_graph(request):
    return render(request,'doc/model_graph.html')
