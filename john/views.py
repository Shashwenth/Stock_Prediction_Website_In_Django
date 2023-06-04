from django.shortcuts import render
from .models import Home,About,Profile,Portfolio,Category,Skills

# Create your views here.

from django.shortcuts import redirect

def link_to_project2(request):
    # Redirect to Project 2's URL
    return redirect('http://127.0.0.1:8000/detail/')

def link_to_project3(request):
    # Redirect to Project 2's URL
    return redirect('http://127.0.0.1:8000/predict/')

def link_to_project1(request):
    # Redirect to Project 2's URL
    return redirect('http://127.0.0.1:8000/compare/')

def index(request):

    home=Home.objects.latest('updated')
    

    #about

    about= About.objects.latest('updated')
    profiles= Profile.objects.filter(about=about)
    categories= Category.objects.all()
    portfolios= Portfolio.objects.all()
    context = {
        'home' : home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios
    }
    return render(request, 'index1.html', context)
