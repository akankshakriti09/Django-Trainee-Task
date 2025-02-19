from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Author, Book

@receiver(post_save, sender=Author)
def create_book(sender, instance, **kwargs):
    print("Signal triggered: Creating a book entry")
    Book.objects.create(title=f"Default Book for {instance.name}", author=instance)
