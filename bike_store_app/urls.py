from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name = 'index'),
    path('cat/<str:id>', views.cat, name = 'cat'),
    path('description/<int:id>/', views.description_view, name = 'description'),
    path('description/<int:id>/add', views.add, name = 'add'),
    path('cart/remove/<int:id>', views.remove, name = 'remove'),
    path('aboutus/', views.about_us_view, name = 'about'),
    path('cart/', views.cart_view, name = 'cart'),
    path('cart/order/<int:id>', views.order, name = 'order'),
    path('order/', views.order_view, name = 'order'),
]
