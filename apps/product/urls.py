from django.urls import path, include
from . import views

# Product 목록 보여주기
product_list = views.ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# Product detail 보여주기 + 수정 + 삭제
product_detail = views.ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns =[
    path('', product_list),
    path('<int:pk>', product_detail),
]