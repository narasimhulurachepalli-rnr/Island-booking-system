from django.urls import path
from . import views

urlpatterns = [
    # Customer endpoints
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/', views.get_customers, name='get_customers'),
    path('customers/update/<int:id>/', views.update_customer, name='update_customer'),
    path('customers/delete/<int:id>/', views.delete_customer, name='delete_customer'),

    # Island endpoints
    path('islands/add/', views.add_island, name='add_island'),
    path('islands/', views.get_islands, name='get_islands'),
    path('islands/update/<int:id>/', views.update_island, name='update_island'),
    path('islands/delete/<int:id>/', views.delete_island, name='delete_island'),

    # Resort & Package endpoints
    path('packages/add/', views.add_package, name='add_package'),
    path('packages/', views.get_packages, name='get_packages'),
    path('packages/update/<int:id>/', views.update_package, name='update_package'),
    path('packages/delete/<int:id>/', views.delete_package, name='delete_package'),

    # Booking endpoints
    path('bookings/add/', views.add_booking, name='add_booking'),
    path('bookings/', views.get_bookings, name='get_bookings'),
    path('bookings/update/<int:id>/', views.update_booking, name='update_booking'),
    path('bookings/delete/<int:id>/', views.delete_booking, name='delete_booking'),

    # Payment endpoints
    path('payments/add/', views.add_payment, name='add_payment'),
    path('payments/', views.get_payments, name='get_payments'),
    path('payments/update/<int:id>/', views.update_payment, name='update_payment'),
    path('payments/delete/<int:id>/', views.delete_payment, name='delete_payment'),
]
