from django.shortcuts import render
from core.models import Package

def gallery_page(request):
    packages = Package.objects.all()
    return render(request, 'gallery/gallery.html', {'packages': packages})
