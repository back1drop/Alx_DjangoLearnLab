from django.db import models

class Author(models.Model):
    """
    Author model:
    Represents a book author with a one-to-many relationship to books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    Each book is linked to an author.
    Includes publication year validation at the serializer level.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
