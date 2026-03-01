from django.urls import path
from .views import home, package_list, package_detail

urlpatterns = [
    path('', home, name='home'),  # ✅ 'home' view is named
    path('packages/', package_list, name='package_list'),
    path('packages/<int:pk>/', package_detail, name='package_detail'),
]




