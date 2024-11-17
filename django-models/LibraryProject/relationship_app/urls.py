from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Views for books and libraries
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views using class-based views
    path('register/', views.register, name='register'),  # Custom register view
    path('login/', views.login_view, name='login'),  # Custom login view
    path('logout/', views.logout_view, name='logout'),  # Custom logout view
]
