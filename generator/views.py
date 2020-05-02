from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')
def password(request):
    characters = list('')
    lower = list('abcdefghijklmnopqrstuvwxyz')
    upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    number = list('01234567890123456789')
    special = list('!@#$&*/()^.,?%$#\|+-<>')
    thepassword = ''
    length = int(request.GET.get('length',12))
    flag=False
    if request.GET.get('lowercase'):
        flag=True
        characters.extend(lower)

    if request.GET.get('uppercase'):
        flag = True
        characters.extend(upper)

    if request.GET.get('numbers'):
        flag = True
        characters.extend(number)

    if request.GET.get('special'):
        flag = True
        characters.extend(special)
    if(flag==False):
        return HttpResponse("<h2><center>you have not selected anything</center></h2>")

    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password': thepassword})

def about(request):
    return render(request,'generator/about.html')
