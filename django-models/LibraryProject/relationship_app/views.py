from django.views.generic.detail import DetailView  # Explicit import for DetailView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book, Library

# Function-based view to list books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
