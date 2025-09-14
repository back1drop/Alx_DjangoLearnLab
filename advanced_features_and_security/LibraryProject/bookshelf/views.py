from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import ExampleForm

@login_required
@permissions_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

#to prevent sql injection, use orms instead of raw sql queries
def book_search(request):
    form = ExampleForm(request.GET or None)
    books = []
    if form.is_valid():
        title = form.cleaned_data['title']
        #secure orm query
        books = Book.objects.filter(title__icontains=title)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
