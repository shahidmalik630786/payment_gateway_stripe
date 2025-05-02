from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:product_id>/', views.CreateCheckoutSessionView.as_view(), name='checkout'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('checkout-page/<int:product_id>/', views.checkout_page, name='checkout_page'),
]