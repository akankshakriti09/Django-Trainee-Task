import threading
import io
from django.shortcuts import render
from .models import TestModel
from django.db.models.signals import post_save
from django.dispatch import receiver

# Capture output
output_buffer = io.StringIO()

@receiver(post_save, sender=TestModel)
def test_signal_handler(sender, instance, **kwargs):
    thread_id = threading.get_ident()
    output_buffer.write(f"Signal Handler Thread ID: {thread_id}\n")

def home_view(request):
    output_buffer.truncate(0)  # Clear previous output
    output_buffer.seek(0)

    thread_id = threading.get_ident()
    output_buffer.write(f"Caller Thread ID (before saving): {thread_id}\n")

    obj = TestModel(name="Test")
    obj.save()

    thread_id_after = threading.get_ident()
    output_buffer.write(f"Caller Thread ID (after saving): {thread_id_after}\n")

    return render(request, 'home.html', {'output': output_buffer.getvalue()})
