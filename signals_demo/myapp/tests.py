from django.db import transaction
from myapp.models import Author, Book

try:
    with transaction.atomic():
        author = Author.objects.create(name="John Doe")  # This triggers the signal
        raise ValueError("Intentional Error!")  # Forces a rollback
except ValueError:
    pass  # Handle the error gracefully

# Check if the Book entry exists
print(Book.objects.exists())  # Should print False if signals run in the same transaction
