import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel

@receiver(post_save, sender=TestModel)
def test_signal_handler(sender, instance, **kwargs):
    print(f"Signal Handler Thread ID: {threading.get_ident()}")
