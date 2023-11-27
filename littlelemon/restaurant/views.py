from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu, Booking
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu': menu_data}
    return render(request, 'menu.html', main_data)

def display_menu_item (request, pk = None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    menu_item_dict = {'menu_item': menu_item}
    return render(request, 'menu_item.html', menu_item_dict)

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 
