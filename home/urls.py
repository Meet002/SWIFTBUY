from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('signup/', views.signup, name='signup'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]