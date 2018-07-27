from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=50)
	number = models.IntegerField()
	prerequisites = models.ForeignKey("self", on_delete=models.PROTECT)
	def __str__(self):
		return self.name