from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def resume(request):
    return render(request, 'resume.html')

def portfolio(request):
    return render(request, 'portfolio.html')
