from django.shortcuts import render, redirect
from .models import ViewBooks, Cart

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        print(request.user.id)
    books = ViewBooks.objects.all()
    try:
        cart = Cart.objects.filter(id_user=request.user.id)
        citems = []
        for i in cart:
            citems.append(i.id_book)
    except:
        cart = ''
    return render(request, 'index.html', {'books': books, 'cart': citems})


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
        return render(request, 'errorpage.html', {'msg': 'You are not logged in'})


def viewBook(request):
    id = request.GET['id']
    book = ViewBooks.objects.get(id=id)
    print(id)
    print(book.BookName)
    return render(request, 'bookinfo.html', {'book': book})


def myBooks(request):
    books = ViewBooks.objects.filter(userid=request.user.email)
    return render(request, 'mybooks.html', {'books': books})


def addcart(request, index):
    cartitems = Cart.objects.filter(id_user=request.user.id)
    cartbooks = []
    for i in cartitems:
        print(i.id_book)
        cartbooks.append(i.id_book)
    if index in cartbooks:
        return redirect('/')
    else:
        Cart.objects.create(id_book=index, id_user=request.user.id)
        return redirect('/')


def myorders(request):
    return render(request, 'myorders.html')


def cart(request):
    return render(request, 'cart.html')


def login(request):
    return render(request, 'loginbook.html')


def register(request):
    return render(request, 'register.html')


def error_404(request, exception):
    return render(request, 'errorpage.html', {'mes': exception})


def error_500(request):
    data = {}
    return render(request, 'errorpage.html')
