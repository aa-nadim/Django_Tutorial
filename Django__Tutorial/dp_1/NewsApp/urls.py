from django.urls import path
from .import views
from .views import NewsP, Home, Contact, NewsDate, register, addUSer, addModalForm, modelform, Customers

urlpatterns = [
    path('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path('newsdate/<int:year>', NewsDate, name='newsdate'),
    path('contact/', Contact, name='contact'),
    path('signup/', register, name='register'),
    path('addUser/', addUSer, name='addUser'),
    path('modalform/', modelform, name='form'),
    path('addmodalform/', addModalForm, name='modalform'),
    path('Customers/', Customers, name='customersinfo'),
]
