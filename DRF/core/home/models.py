from django.db import models
from django.core.validators import FileExtensionValidator


class Student(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(default=18,null=True)
    father_name = models.CharField(max_length=100,null=True)
    pdf_file = models.FileField(validators=[FileExtensionValidator(['pdf'])], upload_to='docs',null=True)
    
    def __str__(self):
        return self.name