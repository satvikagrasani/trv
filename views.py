from django.shortcuts import render
from . models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.img = 'destination_1.jpg'
    dest1.price = 500
    dest1.desc = 'A'

    dest2 = Destination()
    dest2.name = 'Mumbai'
    dest2.img = 'destination_2.jpg'
    dest2.price = 500
    dest2.desc = 'B'

    dest3 = Destination()
    dest3.name = 'Mumbai'
    dest3.img = 'destination_3.jpg'
    dest3.price = 500
    dest3.desc = 'C'
    dests = [dest1,dest2,dest3]

    return render(request,'index.html', {'dests':dests})