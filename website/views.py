from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def home(request):
    return render(request, 'index.html')

def external(request):
    inp = request.POST.get('instrument')
    out1 = run([sys.executable, 'C:/Users/Ciprian/PycharmProjects/AI-music/generate-music/Generate.py', inp],shell=False,stdout=PIPE)
    print(out1.stdout)
    return render(request,'index.html',{'data1':letters(out1.stdout.decode('utf-8')), })

def letters(input):
    return ''.join([c for c in input if c.isalpha()])
