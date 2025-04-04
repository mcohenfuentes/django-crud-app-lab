from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User



DIFFICULTIES = (
    ('E', 'Easy'),
    ('M', 'Medium'),
    ('H', 'Hard')
)

class Mountain(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("mountain-detail", kwargs={"mountain_id": self.id})

class Climb(models.Model):
    date = models.DateField('Date Climbed')
    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTIES,
        default=DIFFICULTIES[0][0]
     )
    
    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_difficulty_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']