from django.shortcuts import render

def home(request):
    return render(request, 'tutorsitekr/home.html',{'nbar':'home'})

def about(request):
    return render(request, 'tutorsitekr/about.html',{'nbar':'about'})

def subjects(request):
    return render(request, 'tutorsitekr/subjects.html',{'nbar':'subjects'})

def pricing(request):
    return render(request, 'tutorsitekr/pricing.html',{'nbar':'pricing'})

def contact(request):
     return render(request, 'tutorsitekr/contact.html',{'nbar':'contact'})
