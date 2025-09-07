from .models import Book, Author, Library

# Query all books by a specific author
def books_by_author(author):
    return Book.objects.filter(author=author)

# List all books in a specific library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian  # because of OneToOneField
