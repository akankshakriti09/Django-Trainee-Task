from django.shortcuts import HttpResponse
from .models import TestModel
import time

def test_signal(request):
    start_time = time.time()

    TestModel.objects.create(name="Testing Django Signals")

    end_time = time.time()
    execution_time = end_time - start_time

    return HttpResponse(f"Signal execution time: {execution_time:.2f} seconds")
