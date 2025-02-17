from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class TestModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TestModel)
def my_sync_signal(sender, instance, **kwargs):
    print("Signal execution started...")
    time.sleep(3)  # Simulating delay
    print("Signal execution completed.")

