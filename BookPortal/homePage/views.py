from django.shortcuts import render
from .models import ViewBooks

# Create your views here.


def home(request):
    books = ViewBooks.objects.all()
    return render(request, 'index.html', {'books': books})


def sellBooks(request):
    return render(request, 'sell_books.html')


def login(request):
    return render(request, 'loginbook.html')


def register(request):
    return render(request, 'register.html')


def error_404(request, exception):
    return render(request, 'errorpage.html', data)


def error_500(request):
    data = {}
    return render(request, 'errorpage.html', data)
