from django.urls import path
from .views import gallery_page

urlpatterns = [
    path('', gallery_page, name='gallery_page'),
]
