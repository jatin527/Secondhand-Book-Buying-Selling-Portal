from django.shortcuts import render, redirect
from .models import ViewBooks

# Create your views here.


def home(request):
    books = ViewBooks.objects.all()
    return render(request, 'index.html', {'books': books})


def sellBooks(request):
    if request.method == 'POST':
        authorName = request.POST['authorname']
        bookname = request.POST['bookname']
        blang = request.POST['blang']
        category = request.POST['category']
        date = '2021-03-30'
        price = request.POST['price']
        img = request.FILES['img']
        bdis = request.POST['bdis']
        bdistdet = request.POST['bdisdet']
        book = ViewBooks(BookName=bookname, language=blang, author=authorName, description=bdistdet, category=category,
                         condition=bdis, price=price, image=img, new=True, userid='testing', purchasedate=date, publisher='testing123')
        book.save()
        return redirect('/')
    else:
        return render(request, 'sell_books.html')


def error_404(request, exception):
    return render(request, 'errorpage.html', {'mes': exception})


def error_500(request):
    data = {}
    return render(request, 'errorpage.html')
