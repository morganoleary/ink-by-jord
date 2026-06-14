from django.shortcuts import render
from .models import TattooImage

#Create your views here

def gallery(request):
    images = TattooImage.objects.all()

    return render(
        request,
        "gallery/gallery.html",
        {"images": images}
    )