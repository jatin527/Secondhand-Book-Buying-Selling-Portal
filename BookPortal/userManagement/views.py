from django.shortcuts import render, redirect
from .models import customerUser
from django.contrib.auth import authenticate


# Create your views here.

def login(request):
    return render(request, 'loginbook.html')


def register(request):
    if request.method=='POST':
        name = request.POST['Name']
        email = request.POST['Email']
        contact = request.POST['Contact']
        city = request.POST['City']
        passw = request.POST['Password']
        user = customerUser.objects.create_user(email = email, name = name, contact_no=contact, city=city, password=passw, username=email)
        user.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username, password)
        if user is not None:
            return redirect('/')
        else:
            return render(request, 'loginbook.html', {"msg":"Invalid Credentials"})
    else:
        return render (request, 'loginbook.html')