# Advanced API Project

## Views & Endpoints

### Book Endpoints

- **GET /api/books/** → List all books
- **GET /api/books/<id>/** → Retrieve a single book
- **POST /api/books/create/** → Create a new book (authenticated only)
- **PUT /api/books/<id>/update/** → Update an existing book (authenticated only)
- **DELETE /api/books/<id>/delete/** → Delete a book (authenticated only)

## Permissions

- Unauthenticated users → Read-only access
- Authenticated users → Can create, update, and delete
- Custom permission `IsAuthorOrReadOnly` available for stricter control

## Advanced Query Features

The `/api/books/` endpoint supports:

### 1. Filtering

Filter by attributes:

- Title → `/api/books/?title=Things Fall Apart`
- Publication year → `/api/books/?publication_year=1958`
- Author (ID) → `/api/books/?author=1`

### 2. Searching

Search text across fields:

- `/api/books/?search=Chinua`
- `/api/books/?search=Fall`

### 3. Ordering

Sort results by field:

- Ascending by title → `/api/books/?ordering=title`
- Descending by year → `/api/books/?ordering=-publication_year`

## Testing

Unit tests are provided in `api/test_views.py` and cover:

- CRUD operations for the Book model
- Filtering, searching, and ordering
- Permission enforcement for authenticated vs. unauthenticated users

### Running Tests

Execute:

```bash
python manage.py test api
```
