from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# ✅ Sign-up view (cleaned)
def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "🎉 Account created successfully!")
            return redirect('sign_in')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# ✅ Sign-in view (cleaned)
def sign_in(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home')  # 👈 Redirects to home after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the errors in the form.")
        return render(request, 'accounts/login.html', {'form': form})
from booking.models import Booking  # import the Booking model

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-start_date')
    return render(request, 'accounts/booking_history.html', {'bookings': bookings})


# ✅ Profile view
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


# ✅ Sign-out view
def sign_out(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('sign_in')
