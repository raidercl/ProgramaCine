from django.contrib import admin

from .models import Director, Movie

# Register your models here.

admin.site.register(Movie)
admin.site.register(Director)