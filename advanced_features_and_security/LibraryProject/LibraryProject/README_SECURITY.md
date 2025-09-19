# Security Configuration (summary)

## Key settings
- DEBUG=False in production (use DJANGO_DEBUG env var)
- SECRET_KEY set via environment variable
- SESSION_COOKIE_SECURE=True, CSRF_COOKIE_SECURE=True
- SECURE_BROWSER_XSS_FILTER=True, SECURE_CONTENT_TYPE_NOSNIFF=True
- X_FRAME_OPTIONS='DENY'
- Content Security Policy header added by `LibraryProject.middleware.StaticCSPHeaderMiddleware`

## Templates
All POST forms include `{% csrf_token %}` and use Django forms for validation.

## Views
- Use Django ORM — no inline SQL.
- Input validated via forms in `bookshelf/forms.py`.
- Authorization enforced via `@permission_required`.

## Testing
Run manual tests for CSRF, CSP, SQL injection and permission enforcement as described in the Testing checklist.
