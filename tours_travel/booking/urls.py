from django.urls import path
from .views import booking_page, package_success

urlpatterns = [
    path('', booking_page, name='booking_page'),            # /booking/
    path('success/', package_success, name='package_success'),  # /booking/success/
]
