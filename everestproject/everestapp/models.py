from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class TimeStamp(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True, null=True,blank=True)

    class Meta:
        abstract = True

class Category(TimeStamp):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category/', null=True,blank=True)

    def __str__(self):
        return self.title

class News(TimeStamp):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete= models.CASCADE, related_name='allnews')
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='news/',null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title
