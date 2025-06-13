from django.shortcuts import render

# Create your views here.

def games_home(request):
    return render(request, 'games/home.html')