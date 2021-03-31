from django.urls import path
from. import views

urlpatterns = [
    path('', views.home),
    path('sellBooks', views.sellBooks),
    path('login', views.login),
    path('register', views.register)
]
