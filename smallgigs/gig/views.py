from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    return HttpResponse("Welcome to SmallGigs.com")

def findgigs(request):
    return HttpResponse('This is the Gig finder place')

def test(resquest):
    return HttpResponse('this is to test the urls')