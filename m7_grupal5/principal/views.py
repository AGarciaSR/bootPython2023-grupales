from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from .models import AppUser
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserForm


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

def users_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user.is_active:
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, "Credenciales incorrectas, inténtelo de nuevo")
                    return render(request, "users_login.html", {"form": form})
        else:
            messages.info(request, "Credenciales incorrectas, inténtelo de nuevo")
            return render(request, "login.html", {"form": form})
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

def users_logout(request):
    logout(request)
    return redirect('index')

def about(request):
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

def user_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User()
            new_user.username = form.cleaned_data['username']
            new_user.password = make_password(form.cleaned_data['password'])
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.email = form.cleaned_data['email']
            new_user.edad = form.cleaned_data['edad']
            new_user.ciudad = form.cleaned_data['ciudad']
            new_user.save()
            print(form)
            print(request.path_info)
            if request.path_info == 'users/user_form':
                new_user.groups.add(Group.objects.get(name=form.cleaned_data['group']))
            else:
                new_user.groups.add(Group.objects.get(name='Cliente'))
            new_id = User.objects.get(username = form.cleaned_data['username']).id
            new_appuser = AppUser.objects.get(user_id = new_id)
            new_appuser.ciudad = request.POST['ciudad']
            new_appuser.edad = request.POST['edad']
            new_appuser.save()
            return HttpResponse("Gracias, el usuario ha sido agregado")
        else:
            if form.errors == 'group':
                form.is_valid
    else:
        form = UserForm()

    return render(request, "user_form.html", {"form": form})