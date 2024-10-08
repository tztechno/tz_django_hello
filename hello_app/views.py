

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, Django!")

def second_page(request):
    return HttpResponse("This is the second page.")

def third_page(request):
    return render(request, 'hello_app/third_page.html')