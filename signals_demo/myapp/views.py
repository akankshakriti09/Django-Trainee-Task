from django.shortcuts import HttpResponse
from django.db import transaction
from myapp.models import Author, Book

def home(request):
    try:
        with transaction.atomic():
            author = Author.objects.create(name="John Doe")  # Triggers signal
            raise ValueError("Intentional Error!")  # Forces rollback
    except ValueError:
        pass  # Handle the error gracefully

    # Check if the Book entry exists
    exists = Book.objects.exists()
    return HttpResponse(f"Book exists after rollback: {exists}")  # Should be False
