from django.shortcuts import render

# Create your views here.

def tools_home(request):
    return render(request, 'tools/home.html')