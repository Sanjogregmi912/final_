from django.urls import path
from booking import views

urlpatterns = [
    path('booking_new/<int:game_id>',views.booking,name="booking_new"),
    path('booking_final',views.bookingfinal,name="booking_final"),
    path('booking_view',views.booking_view,name="booking_view")
]
