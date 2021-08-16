from django.db import models

# Create your models here.

class Singer(models.Model):
	"""
	create model for Singer 
	"""
	name  = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Album(models.Model):
	"""
	Model for albums
    with one to many relation with songs
	"""
	name = models.CharField(max_length=200)
	release_date = models.DateTimeField('release date')

	def __str__(self):
		return self.name

class Song(models.Model):
	"""
	Song Model for songs
    Many to many relation with singer

	"""

	name = models.CharField(max_length=250)
	length = models.DecimalField(max_digits=4,
								      decimal_places=2)
	singer = models.ManyToManyField(Singer)
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
