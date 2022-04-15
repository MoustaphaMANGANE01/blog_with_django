from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def utilisateurs_view(request):
    return render(request,'utilisateurs/liste.html')

