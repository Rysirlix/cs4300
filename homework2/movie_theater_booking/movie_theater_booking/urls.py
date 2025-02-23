from django.contrib import admin
from django.urls import include, path
from bookings.views import MovieViewSet, SeatViewSet, BookingViewSet
from rest_framework.routers import DefaultRouter
from django.shortcuts import redirect

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movies")
router.register(r"seats", SeatViewSet, basename="seats")
router.register(r"bookings", BookingViewSet, basename="bookings")

def redirect_to_movies(request):
    return redirect("movie_list")

urlpatterns = [
    path('bookings/', include('bookings.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('',  redirect_to_movies, name="movies"),
]