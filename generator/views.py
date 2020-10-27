from django.shortcuts import render
from django.http import HttpResponse
import random
import string


def about(req):
    return  render(req ,'generator/about.html')

def home(req):
    return render(req, 'generator/home.html', {'pass': ''})


def password(request):
    s1 = []
    # n=int(request.Get.get('length'))
    n = int(request.GET.get('len'))
    met1 = request.GET.get("up")
    met3 = request.GET.get('dig')
    met2 = request.GET.get('spec')
    x = (f'met1:{met1}\nmet2 : {met2}\nmet3: {met3}')
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    special = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    dig = string.digits

    l1 = lower
    if request.GET.get("up"):
        l1 += upper
    if request.GET.get('dig'):
        l1 += dig
    if request.GET.get('spec'):
        l1 += special

    l1 = list(l1)
    for i in range(n):
        q = random.randint(0, len(l1) - 1)
        s1.append(l1[q])

    password1 = ''.join(s1)
    return render(request, 'generator/pass.html', {'pass': password1, 'x': x})
