from django.urls import path
from .views import test_signal

urlpatterns = [
    path('test-signal/', test_signal, name='test_signal'),
]
