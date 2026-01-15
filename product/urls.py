from django.urls import path
from .views import shop, shop_detail, ShopListView, ShopDetailView

urlpatterns = [
    path('shop/', ShopListView.as_view(), name = 'shop'),
    path('shop/<str:slug>/', ShopDetailView.as_view(), name = 'shop-detail')
]
