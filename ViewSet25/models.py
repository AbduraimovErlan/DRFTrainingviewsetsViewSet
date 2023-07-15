from django.db import models

# Create your models here.
class Book25(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()


    def __str__(self):
        return self.title