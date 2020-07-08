from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):
    length = int(request.GET.get('length',10))

    character = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get("uppercase"):
        character.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("special"):
        character.extend(list("@#%^&*!"))
    if request.GET.get("numbers"):
        character.extend(list("0123456789"))

    password1 =''

    for x in range(length):
        password1 += random.choice(character)
    return render(request,'generator/password.html',{'password':password1})
