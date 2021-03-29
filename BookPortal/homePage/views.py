from django.shortcuts import render
from .models import ViewBooks

# Create your views here.


def home(request):
    books = ViewBooks.objects.all()
    return render(request, 'index.html', {'books': books})
