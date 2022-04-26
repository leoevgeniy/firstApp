from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def figma(request):
    return render(request, 'main/figma.html')
