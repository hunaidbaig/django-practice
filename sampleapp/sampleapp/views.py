from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    print(request)
    # return HttpResponse("Hello, from home page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello, from about page")

def contact(request):
    return HttpResponse("Hello, from contact page")