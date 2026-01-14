from django.urls import path
from .views import homepage, about, contact, ContactView

urlpatterns = [
    path('', homepage, name = 'home'),
    path('about/', about, name='about'),
    path('contact/', ContactView.as_view(), name= 'contact')
]
