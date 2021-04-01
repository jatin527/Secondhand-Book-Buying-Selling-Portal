from django.shortcuts import render, redirect
from .models import ViewBooks

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        print(request.user.id)
    books = ViewBooks.objects.all()
    return render(request, 'index.html', {'books': books})


def sellBooks(request):
    if request.user.is_authenticated:
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
                                condition=bdis, price=price, image=img, new=True, userid=request.user.email, purchasedate=date, publisher='testing123')
                book.save()
                return redirect('/')
            else:
                return render(request, 'sell_books.html')
    else:
        return render(request, 'errorpage.html', {'msg':'You are not logged in'})


def viewBook(request):
    id = request.GET['id']
    book = ViewBooks.objects.get(id=id)
    print(id)
    print(book.BookName)
    return render(request, 'viewBooks.html', {'book':book})


def login(request):
    return render(request, 'loginbook.html')


def register(request):
    return render(request, 'register.html')


def error_404(request, exception):
    return render(request, 'errorpage.html', {'mes': exception})


def error_500(request):
    data = {}
    return render(request, 'errorpage.html')
