from django.urls import path, include
from . import views

# order 목록 보여주기
order_list = views.OrderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# order detail 보여주기 + 수정 + 삭제
order_detail = views.OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns =[
    path('', order_list),
    path('<int:pk>', order_detail),
]