from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Brian'}) # home page rendered


def add(request):
    #python code to add 2 numbers
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result':res}) # When add is called, result will appear after converted to Jinja format