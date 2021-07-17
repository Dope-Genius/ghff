from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  overview = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)
  author = models.CharField(max_length=50)
  thumbnail = models.ImageField()

  def __str__(self):
    return self.title