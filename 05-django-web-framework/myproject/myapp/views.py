from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu

def home(request):
    return HttpResponse("Welcome to Little Lemon!")

def about(request):
    about_content = {
        'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."
    }
    return render(request, 'about.html', {'content': about_content})

def menu(request):
    menu_items = Menu.objects.all()
    items_dict = {'menu': menu_items}
    return render(request, 'menu.html', items_dict)

def book(request):
    return HttpResponse("Make a booking")

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})