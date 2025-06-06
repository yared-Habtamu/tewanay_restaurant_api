from django.urls import path
from .views import TableBookingCreateView, AllBookingsListView, MyBookingsListView

urlpatterns = [
    path('', TableBookingCreateView.as_view(), name='booking-create'),  # POST (Customer)
    path('all/', AllBookingsListView.as_view(), name='all-bookings'),  # GET (Manager/Admin)
    path('mine/', MyBookingsListView.as_view(), name='my-bookings'),   # GET (Customer)

]