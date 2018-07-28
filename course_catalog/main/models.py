from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=100)
	number = models.IntegerField()
	prerequisites = models.ManyToManyField("self", null=True, blank=True, symmetrical=False, related_name="prereqs")
	def __str__(self):
		return self.name