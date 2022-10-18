from pickle import FALSE
from pydoc import ModuleScanner
from xml.etree.ElementTree import Comment
from django import forms
from .models import Movie
from django.forms import  ModelForm



class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = ['name', 'comment']

    

