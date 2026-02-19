from django.urls import path
from .views import homepage, about, contact, ContactView, export_view

urlpatterns = [
    path('', homepage, name = 'home'),
    path('about/', about, name='about'),
    path('export/', export_view, name = 'export'),
    path('contact/', ContactView.as_view(), name= 'contact')
]
