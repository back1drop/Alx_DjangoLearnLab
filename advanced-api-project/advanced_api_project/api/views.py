from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions,filters
from .models import Book
from .serializers import BookSerializer

"""
Generic views for the Book model.
We use DRF’s built-in generic views to handle CRUD operations efficiently.
"""

class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books with support for:
    - Filtering (by title, author, publication_year)
    - Searching (by title and author name)
    - Ordering (by title, publication_year, or any other field)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching
    search_fields = ['title', 'author__name']  # note the double underscore for related field lookup

    # Ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by its ID.
    Accessible to all users (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
