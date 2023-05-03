from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    emotion = models.CharField(max_length=200)
    weather = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
        