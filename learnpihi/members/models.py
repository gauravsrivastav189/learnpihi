from django.db import models

# Create your models here.
class Members(models.Model):
	course_name=models.CharField(max_length=255)
	star_rating=models.IntegerField()
	comments=models.TextField()
	
	
