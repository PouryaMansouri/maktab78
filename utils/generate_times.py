from datetime import timedelta
from django.utils import timezone


def two_min_from_now():
    return timezone.now() + timedelta(minutes=2)
