
from django.http import HttpResponse
from django.shortcuts import render
def first_page(request):
    return HttpResponse('Hello Fronted')
def info(request):
    return HttpResponse('<h1>Hello Fronted<h1>')
def main_page(request):
    return render(request, "about.html")
def buttom(request):
    return render(request, "buttom.html")
def index(request):
    return render(request,'wepap/index.html')