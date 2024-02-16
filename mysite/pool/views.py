from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world. This is the pool index')

def add_game(request):
    return HttpResponse("Add a game of pool")

def results(request, start_date, end_date):
    return HttpResponse("Viewing results")
