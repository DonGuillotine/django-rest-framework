from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_alternate_view),
    path('<int:pk>/', views.product_alternate_view),
]