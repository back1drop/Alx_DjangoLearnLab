from django.urls import path
from .views import list_books, LibraryDetailView, register_view, login_view, logout_view
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path("books/", views.list_books, name="list_books"),   
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  
      # Authentication
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

     path("admin-page/", admin_view, name="admin_view"),
    path("librarian-page/", librarian_view, name="librarian_view"),
    path("member-page/", member_view, name="member_view"),
        # Secured book actions
    path("books/add/", add_book, name="add_book"),
    path("books/<int:book_id>/edit/", edit_book, name="edit_book"),
    path("books/<int:book_id>/delete/", delete_book, name="delete_book"),

]
