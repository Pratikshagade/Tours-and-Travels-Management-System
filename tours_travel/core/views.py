from django.shortcuts import render, get_object_or_404
from .models import Package

def home(request):
    return render(request, 'core/home.html')

def package_list(request):
    packages = Package.objects.all()
    return render(request, 'core/package_list.html', {'packages': packages})

# ✅ NEW view to show one package in detail
def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)
    return render(request, 'core/package_detail.html', {'package': package})
