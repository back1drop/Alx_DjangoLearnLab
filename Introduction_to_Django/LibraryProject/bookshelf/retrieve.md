# Retrieve Book

```python
from bookshelf.models import Book

# Retrieve the book we created
book = Book.objects.get(title="1984")

book
# Expected Output:
# <Book: 1984 by George Orwell>
