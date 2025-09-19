# bookshelf/forms.py

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        # Additional sanitization if you want to reject suspicious input
        # e.g. remove script tags (though CSP + autoescape will handle most XSS)
        return title

class BookSearchForm(forms.Form):
    q = forms.CharField(max_length=200, required=False)

    def clean_q(self):
        q = self.cleaned_data.get("q", "").strip()
        # reject extremely long or suspicious values
        return q
