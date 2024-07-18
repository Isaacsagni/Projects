from django.shortcuts import render
from .models import Cloth


# Create your views here.
def index (request):
    Cloths = Cloth.objects.all()

    return render(request, 'index.html', {'Cloths' : Cloths}) # home page rendered