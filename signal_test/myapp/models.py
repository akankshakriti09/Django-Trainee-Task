import threading
from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        print(f"Caller Thread ID (before saving): {threading.get_ident()}")
        super().save(*args, **kwargs)
        print(f"Caller Thread ID (after saving): {threading.get_ident()}")
