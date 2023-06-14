from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    return render(request, "index.html")

def users(request):
    user_details = User.objects.only('id','username','first_name','last_name','email','appuser')
    '''user_details = User.objects.all()'''
    print (user_details)
    context = {
        'appusers' : user_details
    }
    return render(request, "users.html", context)

def user_detail(request,id_number):
    user_details = User.objects.only('id','username','first_name','last_name','email','appuser').filter(id=id_number)
    context = {
        'usuario' : user_details
    }
    return render(request, "user_detail.html", context)

def about(request):
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')