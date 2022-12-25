from django.db import models
from django.urls import reverse
# Create your models here.

class New(models.Model):
     title = models.CharField(max_length=50)
     text = models.TextField()

     def __str__(self):
          return self.title

class Post(models.Model):
     title = models.CharField(max_length=30)
     author = models.ForeignKey(
          'auth.User',
          on_delete=models.CASCADE
     )
     text = models.TextField()

     def get_absolute_url(self):
          return reverse('post_detail', args=[str(self.id)])

# class SignUpUsers(models.Model):
#      name = models.CharField(max_length=30)
#      password = models.CharField(max_length=50)
#      def get_absolute_url(self):
#           return reverse('home')