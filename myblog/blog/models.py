from django.db import models
from datetime import datetime






class Author(models.Model):
    name = models.CharField(max_length = 120)
    display_pic = models.ImageField(upload_to="images")
    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length = 120)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    desc = models.TextField()
    date = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.title    
    