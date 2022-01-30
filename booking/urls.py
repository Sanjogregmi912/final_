from django.urls import path
from booking import views

urlpatterns = [
    path('booking_new/<int:game_id>',views.booking),
    path('booking_final',views.bookingfinal),
    path('booking_view',views.booking_view)
]
