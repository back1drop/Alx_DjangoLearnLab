# LibraryProject/middleware.py

from django.utils.deprecation import MiddlewareMixin

class StaticCSPHeaderMiddleware(MiddlewareMixin):
    """
    Adds a conservative Content-Security-Policy header.
    Adjust directives to include domains required by the app (CDNs, analytics, etc.).
    """
    def process_response(self, request, response):
        # Minimal safe CSP for this app - allows same-origin only for scripts/styles/images.
        csp = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self' 'unsafe-inline'; "  # unsafe-inline may be needed if using inline styles — prefer nonce-based approach
            "img-src 'self' data:; "
            "font-src 'self'; "
            "object-src 'none'; "
            "frame-ancestors 'none'; "
            "base-uri 'self';"
        )
        # Do not overwrite if already present
        if "Content-Security-Policy" not in response:
            response["Content-Security-Policy"] = csp
        return response
