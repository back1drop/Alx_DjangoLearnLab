# Permissions & Groups Setup

This project demonstrates custom Django permissions and group-based access control.

## Custom Permissions
Defined in `Book` model (`bookshelf/models.py`):
- can_view → View book list/details
- can_create → Add new book
- can_edit → Edit book
- can_delete → Delete book

## Groups
Configured in `bookshelf/admin.py`:
- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → can_view, can_create, can_edit, can_delete

## Usage
- Assign users to groups in Django Admin.
- Views are protected using `@permission_required`.
- Example:
  ```python
  @permission_required('bookshelf.can_edit', raise_exception=True)
  def book_edit(request, pk):
      ...
