from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):

    characters = list ('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!#@$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    len= int(request.GET.get('length',8))
    var=''

    for x in range(len):
        var += random.choice(characters)
    return render(request,'generator/password.html',{'pass':var})

def about(request):
    return render(request,'generator/about.html')
