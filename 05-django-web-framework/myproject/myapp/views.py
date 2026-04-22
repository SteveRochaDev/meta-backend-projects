from django.shortcuts import render
from .forms import BookingForm
from .models import Menu

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def book(request):
    return render(request, 'book.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})