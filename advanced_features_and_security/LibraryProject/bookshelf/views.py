# bookshelf/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book
from .forms import BookForm, BookSearchForm
from django.db.models import Q

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()
    if form.is_valid():
        q = form.cleaned_data.get("q")
        if q:
            # safe ORM filter (parameterized)
            books = books.filter(Q(title__icontains=q) | Q(author__icontains=q))
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})


@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})


@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/form_example.html", {"form": form, "book": book})


@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    # Render a confirmation page
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})
