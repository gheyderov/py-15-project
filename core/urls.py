from django.urls import path
from .views import homepage, about, contact

urlpatterns = [
    path('', homepage, name = 'home'),
    path('about/', about, name='about'),
    path('contact/', contact, name= 'contact')
]
