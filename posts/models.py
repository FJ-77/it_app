from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=30)
	text = models.TextField()

	def __str__(self):
		return self.title

class Advertisement(models.Model):
	title = models.CharField(max_length=30)
	text = models.TextField()
	creationdate = models.DateField()
	view_num = models.IntegerField()

	def __str__(self):
		return self.title