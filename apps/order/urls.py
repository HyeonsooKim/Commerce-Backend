from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'category', views.CategoryViewSet)

urlpatterns =[
    path('', include(router.urls)),
]