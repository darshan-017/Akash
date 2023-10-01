from django.db import models
from datetime import datetime

class Photo(models.Model):
    CATEGORIES = [
        ("animals", "Animals"),
        ("weeding", "Weeding"),
        ("birthday", "Birth Day"),
        ("nature", "Nature"),
    ]
    name = models.CharField(max_length=60, null=True, blank=True)
    category = models.CharField(max_length=15, choices=CATEGORIES)
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField()
    photo = models.ImageField(upload_to="Photos")
    order_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class ContactInfo(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    address = models.TextField(null=True, blank=True)
    discuss_about = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name