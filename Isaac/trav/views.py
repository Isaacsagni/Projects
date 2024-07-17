from django.shortcuts import render
from .models import Cloth


# Create your views here.

def index(request):

    Cloth1 = Cloth() 
    Cloth1.name = 'Casual Shirt'
    Cloth1.price = 65
    Cloth1.img = 'p1.png'

    Cloth2 = Cloth()
    Cloth2.name = 'Track Suit'
    Cloth2.price = 85
    Cloth2.img = 'p8.png'

    Cloth3 = Cloth()
    Cloth3.name = "Men's Shirt"
    Cloth3.price = 70
    Cloth3.img = 'p10.png'

    Cloths = [Cloth1, Cloth2, Cloth3]
    return render(request, 'index.html', {'Cloths' : Cloths}) # home page rendered