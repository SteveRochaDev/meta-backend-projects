from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm

def home(request):
    return HttpResponse("Welcome to Little Lemon!")

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu")

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