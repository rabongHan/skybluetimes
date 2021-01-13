from django.db import models

# Create your models here.
class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    