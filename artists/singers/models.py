from django.db import models

# Create your models here.

class Singer(models.Model):
	"""
	create model for Singer 
	"""
<<<<<<< HEAD
	name  = models.CharField(max_length=250)
=======
	singer_name  = models.CharField(max_length=250)
>>>>>>> fdc7569ec80ea4c0da0033c964b10b17133de6ee

	def __str__(self):
		return self.name

class Album(models.Model):
<<<<<<< HEAD
=======
	"""
	Model for albums
    with one to many relation with songs
	"""
	album_name = models.CharField(max_length=200)
	release_date = models.DateTimeField('release date')

	def __str__(self):
		return self.album_name

class Song(models.Model):
>>>>>>> fdc7569ec80ea4c0da0033c964b10b17133de6ee
	"""
	Model for albums
    with one to many relation with songs
	"""
<<<<<<< HEAD
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
=======

	song_name = models.CharField(max_length=250)
	song_length = models.DecimalField(max_digits=4,
								      decimal_places=2)
	singer = models.ManyToManyField(Singer)
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	def __str__(self):
		return self.song_name
>>>>>>> fdc7569ec80ea4c0da0033c964b10b17133de6ee
