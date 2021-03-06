from cgi import print_form
from django.shortcuts import redirect, render

from booking.forms import BookingForm
from games.models import Games
from booking.models import Booking
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def booking(request,game_id):
    if request.method == 'POST':
        form= BookingForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                request.session.clear()
                return redirect("games/allgames")
            except:
                print("validation failed")
    else:
        form =BookingForm()
        print("invalid")
    game = Games.objects.get(id=game_id)
    return render(request,'booking/booking_new.html',{'form':form , 'game_id':game_id,'game':game})
@login_required(login_url='/login') 
def bookingfinal(request):
    if request.method == "POST":
        form =BookingForm(request.POST)
        print(form)
        if form.is_valid:
            try:
                print("valid")
                form.save()
                request.session.clear()
                return redirect("/games/games_all")
            except:
                print("Failed")
    else:
        form=BookingForm()
        print("invalid")
    return(request,'booking/booking_new.html',{'form':form})

@login_required(login_url='/login')
def booking_view(request):
    bookings =Booking.objects.raw("select * from booking_booking ")
    return render(request,'booking/booking_view.html' ,{'bookings':bookings})