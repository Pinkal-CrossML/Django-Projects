from django.db import models

# Create your models here.

class Singer(models.Model):
	"""
	create model for Singer 
	"""
	singer_name  = models.CharField(max_length=250)
	singer_id = models.IntegerField()

	def __str__(self):
		return self.singer_name

class Song(models.Model):
	"""
	Song Model for songs
    Many to many relation with singer

	"""

	song_name = models.CharField(max_length=250)
	song_genre = models.CharField(max_length=200)
	song_length = models.DurationField()
	singer = models.ManyToManyField(Singer)

	def __str__(self):
		return self.song_name


class Album(models.Model):
	"""
	Model for albums
    with one to many relation with songs
	"""
	song = models.ForeignKey(Song, on_delete=models.CASCADE)
	album_name = models.CharField(max_length=200)
	release_date = models.DateTimeField('release date')

	def __str__(self):
		return self.album_name