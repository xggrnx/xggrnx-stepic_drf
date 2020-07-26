from django.urls import path
from api.views.recipients import recipient_list, recipient_detail
from api.views.goods import goods_list, goods_detail

urlpatterns = [
    path('recipients/', recipient_list, name='recipient-list'),
    path('recipients/<int:pk>/', recipient_detail, name='recipient-detail'),
    path('goods-sets/', goods_list, name='product-sets'),
    path('goods-sets/<int:pk>/', goods_detail, name='product-detail'),
]
