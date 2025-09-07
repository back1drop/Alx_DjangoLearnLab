from .models import Book, Author, Library


all_books = Book.objects.all()

def books_by_author(author):
    return Book.objects.filter(author=author)

def get_book_by_title(title):
    return Book.objects.get(title=title)

def libraries_with_book(book):
    return Library.objects.filter(books=book)

def books_published_after(year):
    return Book.objects.filter(publication_year__gt=year)
