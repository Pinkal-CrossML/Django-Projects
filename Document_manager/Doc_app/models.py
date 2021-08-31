from os import name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from .validators import validate_file_extension,file_size
class Document(models.Model):
    """
    this model will take input doc file(.pdf format and not more then 5mb) from user and store that in database 
    """
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/', validators=[validate_file_extension,file_size])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    