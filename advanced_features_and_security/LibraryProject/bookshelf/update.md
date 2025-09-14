book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Expected: Book title updated
