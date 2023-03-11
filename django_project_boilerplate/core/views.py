from django.shortcuts import render
from .models import Artwork


def homepage(request):
    return render(request, 'homepage.html')


def gallery(request):
    artworks = Artwork.objects.all()
    context = {
        'artworks': artworks
    }
    return render(request, 'gallery.html', context)
