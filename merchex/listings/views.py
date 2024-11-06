from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello django</h1>")

def about(request):
    return HttpResponse("<h1> A propos !</h1> <p>nous adorons le merch</p>")

def listings(request):
    return HttpResponse("<h1>listing</h1> <p>merch</p>")

def contact(request):
    return HttpResponse("<h1>contact</h1> <p>merch</p>")
    