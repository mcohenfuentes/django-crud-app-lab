from django.db import models
from django.urls import reverse

class Mountain(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("mountain-detail", kwargs={"mountain_id": self.id})
    