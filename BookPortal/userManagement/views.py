from django.shortcuts import render, redirect
from .models import customerUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import auth


# Create your views here.

def login(request):
    return render(request, 'loginbook.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        contact = request.POST['Contact']
        city = request.POST['City']
        passw = request.POST['Password']
        user = customerUser.objects.create_user(
            email=email, name=name, contact_no=contact, city=city, password=passw, username=email)
        user.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = str(request.POST['username']).lower()
        password = request.POST['password']
        try:
            user = customerUser.objects.get(username=username)
            if check_password(password, user.password):
                user = auth.authenticate(
                    request, username=username, password=password)
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'loginbook.html', {'msg': 'Invalid Credentials'})
        except Exception as e:
            return render(request, 'loginbook.html', {'msg': 'Invalid Credentials' + str(e)})
    else:
        return render(request, 'loginbook.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
