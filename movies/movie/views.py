from ast import Return
from operator import index
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(
        request,
        'index.html'
    )