from django.views.generic.detail import DetailView  # Import for class-based views
from django.shortcuts import render
from .models import Book  # Import Book model
from .models import Library  # Import Library explicitly for the checker

# Function-based view to list all books
def list_books(request):
    """
    Displays a list of all books.
    """
    books = Book.objects.all()  # Query all books
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render the list_books template with books context

# Class-based view for library details
class LibraryDetailView(DetailView):
    """
    Displays details of a specific library, including its books.
    """
    model = Library  # Use the Library model
    template_name = 'relationship_app/library_detail.html'  # Template for rendering the library details
    context_object_name = 'library'  # Name used to reference the library in the template
