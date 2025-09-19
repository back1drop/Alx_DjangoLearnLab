Authentication:

- Obtain a token by POSTing username and password to /api-token-auth/
- Include the token in requests using the header:
  Authorization: Token <your_token>

Permissions:

- By default, all API endpoints require authentication.
- BookViewSet requires users to be authenticated.
- Customize permission_classes in views.py for role-based access.
