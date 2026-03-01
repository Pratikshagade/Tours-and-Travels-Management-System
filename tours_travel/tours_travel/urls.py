from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main routes
    path('', include('core.urls')),  # ✅ Home and packages
    path('accounts/', include('accounts.urls')),
    path('booking/', include('booking.urls')),
    path('destination/', include('destination.urls')),
    path('food/', include('food.urls')),
    path('hotel/', include('hotel.urls')),
    path('gallery/', include('gallery.urls')),

]

# ✅ Serve media files (like uploaded images) in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
