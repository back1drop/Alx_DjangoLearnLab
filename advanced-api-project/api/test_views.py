from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints:
    - CRUD operations
    - Filtering, searching, ordering
    - Permissions and authentication
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create an author
        self.author = Author.objects.create(name="Chinua Achebe")

        # Create sample books
        self.book1 = Book.objects.create(title="Things Fall Apart", publication_year=1958, author=self.author)
        self.book2 = Book.objects.create(title="No Longer at Ease", publication_year=1960, author=self.author)

        # Define endpoints
        self.list_url = reverse("book-list")
        self.create_url = reverse("book-create")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.pk})
        self.update_url = reverse("book-update", kwargs={"pk": self.book1.pk})
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book1.pk})

    # ---------- CRUD TESTS ----------

    def test_list_books(self):
        """Test retrieving the list of books (public access allowed)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book_authenticated(self):
        """Test that an authenticated user can create a new book."""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Arrow of God", "publication_year": 1964, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create a book."""
        data = {"title": "Man of the People", "publication_year": 1966, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Test that an authenticated user can update a book."""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Things Fall Apart (Updated)", "publication_year": 1959, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Things Fall Apart (Updated)")

    def test_update_book_unauthenticated(self):
        """Test that unauthenticated users cannot update a book."""
        data = {"title": "Unauthorized Update", "publication_year": 2000, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        """Test that an authenticated user can delete a book."""
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_delete_book_unauthenticated(self):
        """Test that unauthenticated users cannot delete a book."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------- FILTER / SEARCH / ORDER TESTS ----------

    def test_filter_books_by_publication_year(self):
        """Test filtering books by publication year."""
        response = self.client.get(self.list_url, {"publication_year": 1958})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Things Fall Apart")

    def test_search_books_by_title(self):
        """Test searching for books by title."""
        response = self.client.get(self.list_url, {"search": "No Longer"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "No Longer at Ease")

    def test_order_books_by_publication_year_descending(self):
        """Test ordering books by publication year (descending)."""
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "No Longer at Ease")  # 1960 comes first
