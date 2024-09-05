from django.urls import path
from . import views
from .views import CBVView

urlpatterns = [
    path('', views.index, name="index"),
    path('cbv/', CBVView.as_view(), name="cbv"),
    path('product/<int:product_id>/', views.product_detail, name="productDetail"),
]
