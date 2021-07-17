from django.db import models
from django.urls import reverse
from tinymce import HTMLField


class Category(models.Model):
  title = models.CharField(max_length=20)

  def __str__(self):
    return self.title


class Post(models.Model):
  # slug = models.SlugField(max_length=200)
  title = models.CharField(max_length=100)
  overview = models.TextField()
  content = HTMLField('Content')
  timestamp = models.DateTimeField(auto_now_add=True)
  author = models.CharField(max_length=50)
  thumbnail = models.ImageField(upload_to='photos/')
  thumbnail_2 = models.ImageField(upload_to='photos/', blank=True)
  featured = models.BooleanField()
  work = models.BooleanField()
  categories = models.ManyToManyField(Category)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("post_details", kwargs={"id": self.id})
  

class Contact(models.Model):
  fullname = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  subject = models.CharField(max_length=100)
  message = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.fullname