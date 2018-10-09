from django.shortcuts import render

def home(request):
    return render(request, 'tutorsite/home.html',{'nbar':'home'})

def about(request):
    return render(request, 'tutorsite/about.html',{'nbar':'about'})

def subjects(request):
    return render(request, 'tutorsite/subjects.html',{'nbar':'subjects'})

def pricing(request):
    return render(request, 'tutorsite/pricing.html',{'nbar':'pricing'})

def contact(request):
     return render(request, 'tutorsite/contact.html',{'nbar':'contact'})
