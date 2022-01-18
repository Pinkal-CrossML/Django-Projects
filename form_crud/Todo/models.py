from django.db import models

class Todolist(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    status_choices = (
        ('Done', 'Done'),
        ('Pending', 'Pending'),
        ('Progress', 'progress'),
    )
    status = models.CharField(max_length=10, choices=status_choices)
    date = models.DateField()
    
    def __str__(self):
        return self.task_name
    
 