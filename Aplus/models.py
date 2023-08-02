from django.db import models

# Create your models here.
class Algebra(models.Model):
    """algebra questions"""
    text = models.CharField(max_length=200)

    def __str__(self):
        """return a string representation of the model"""
        return self.text
