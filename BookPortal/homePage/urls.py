from django.urls import path
from. import views

urlpatterns = [
    path('', views.home),
    path('sellBooks', views.sellBooks),
    path('viewBook', views.viewBook),
    path('myBooks', views.myBooks),
    path('viewCart', views.cart),
    path('addtoCart/<int:index>', views.addcart),
    path('myOrders', views.myorders),
    path('removecart/<int:index>', views.removecart),
    path('filtercat/<str:cat>', views.filtercat),
    path('filtertype/<str:type>', views.filtertype),
    path('address', views.add),
    path('payment', views.paym),
    path('paydone', views.paydone)
]
