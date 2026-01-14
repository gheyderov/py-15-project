from django.urls import path
from .views import shop, shop_detail, ShopListView

urlpatterns = [
    path('shop/', ShopListView.as_view(), name = 'shop'),
    path('shop/<int:pk>/', shop_detail, name = 'shop-detail')
]
