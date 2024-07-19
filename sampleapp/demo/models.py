from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVarity(models.Model):
    CHAI_CHOICES = [
        ('PL', 'PLAIN'),
        ('GR', 'GINGER'),
        ('KI', 'KIWI'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai/')
    date_time = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_CHOICES)

    def __str__(self):
        return self.name
