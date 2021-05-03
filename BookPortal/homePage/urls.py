from django.urls import path
from. import views

urlpatterns = [
    path('', views.home),
    path('sellBooks', views.sellBooks),
    path('viewBook', views.viewBook),
    path('myBooks', views.myBooks),
    path('viewCart', views.cart),
    path('addtoCart/<int:index>', views.addcart),
    path('myOrders', views.myorders)
]
