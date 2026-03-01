import razorpay
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required  # ✅ Import this
from core.models import Package
from .models import Booking


@login_required
def booking_page(request):
    package_id = request.GET.get('package_id')
    if not package_id:
        return HttpResponse("❌ No package ID provided in URL!")

    package = get_object_or_404(Package, id=package_id)

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    amount_paise = int(package.price * 100)

    payment = client.order.create({
        'amount': amount_paise,
        'currency': 'INR',
        'payment_capture': '1'
    })

    context = {
        'package': package,
        'order_id': payment['id'],
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'amount': amount_paise,
    }
    return render(request, 'booking/booking_page.html', context)


@csrf_exempt
@login_required
def package_success(request):
    if request.method == "POST":
        try:
            user = request.user
            package_id = request.POST.get('package_id')
            package = get_object_or_404(Package, id=package_id)

            # Save booking
            Booking.objects.create(
                user=user,
                package=package,
                razorpay_order_id=request.POST.get('razorpay_order_id'),
                razorpay_payment_id=request.POST.get('razorpay_payment_id'),
                razorpay_signature=request.POST.get('razorpay_signature'),
                name=package.name,
                description=package.description,
                price=package.price,
                start_date=package.start_date,
                end_date=package.end_date,
                image=package.image,
                hotel=package.hotels.first(),
                destination=package.destination,
                address=package.destination.address_set.first() if hasattr(package.destination, 'address_set') else None,
            )

            return render(request, 'booking/payment_page.html', {
                'package': package,
                'payment_id': request.POST.get('razorpay_payment_id')
            })

        except Exception as e:
            print("❌ Error during booking:", e)
            return HttpResponseBadRequest("Something went wrong.")

    return HttpResponseBadRequest("Invalid request method.")
