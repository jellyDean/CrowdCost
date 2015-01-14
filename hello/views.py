from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Users
from django import db


# Create your views here.
def index(request):

    db_request(request)
    return HttpResponse('Hello from Python SAM IS ONLINE')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def db_request(request):
    for p in Users.objects.raw('SELECT * FROM localtable.users'):
        print(p)



