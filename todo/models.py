 
import datetime
from django.db import models

# Create your models here.


class Todo(models.Model):
    COLORS = (
        ('red', 'Red'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    favorite_color = models.CharField(choices=COLORS,max_length=10)
    date_of_birth = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title + '-' + str(self.description)
