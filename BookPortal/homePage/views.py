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
        citems = ''

    return render(request, 'index1.html', {'books': books, 'cart': citems})


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
            try:
                audio = request.FILES['audio']
                book = ViewBooks(BookName=bookname, language=blang, author=authorName, description=bdistdet, category=category,
                             condition=bdis, price=price, image=img, new=True, userid=request.user.email, purchasedate=date, publisher='testing123', audio=audio)
            except:
                
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
    try:
        cart = Cart.objects.filter(id_user=request.user.id)
        citems = []
        for i in cart:
            citems.append(i.id_book)
    except:
        cart = ''
    return render(request, 'bookinfo.html', {'book': book, 'cart': citems})


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


def removecart(request, index):
    c = Cart.objects.get(id_user=request.user.id, id_book=index)
    c.delete()

    return redirect('/')


def payment(request):
    return render(request, 'payment.html', {'cart': 'cart'})


def myorders(request):
    return render(request, 'myorders.html')


def cart(request):
    cart = Cart.objects.filter(id_user=request.user.id)
    book = []
    if cart.__len__ == 0:
        cart = ''
    else:
        for i in cart:
            book.append(i.id_book)
        books = []
        for i in book:
            book = ViewBooks.objects.get(id=i)
            books.append(book)

    if cart == '':
        sendbooks = 'empty'
    else:
        sendbooks = books

    gtotal = 0
    for book in books:
        gtotal += int(book.price)

    return render(request, 'cart.html', {'books': sendbooks, 'total': gtotal})


def login(request):
    return render(request, 'loginbook.html')


def register(request):
    return render(request, 'register.html')


def error_404(request, exception):
    return render(request, 'errorpage.html', {'mes': exception})


def error_500(request):
    data = {}
    return render(request, 'errorpage.html')
