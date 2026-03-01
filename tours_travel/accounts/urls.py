from django.urls import path
from . import views 
from .views import booking_history

urlpatterns = [
    path('sign-up',views.sign_up,name='sign_up'),
    path('sign-in',views.sign_in,name='sign_in'),
    path('sign-out',views.sign_out,name='sign_out'),
    path('profile',views.profile,name='profile'),
    path('history/',booking_history, name='booking_history'),
]